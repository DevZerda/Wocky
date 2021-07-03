# Modules
import os, sys, time, random

# Files
from ..auth.main import *
from ..auth.crud import *
from ..Logger.main import *
from ..banner_system.modify import *
from ..Config.main import *
from ..utils.main import *
from ..Config.functions import *

buffer_length = 1024

def MainScreen(socket, addr):
    socket.send(str(Strings.MainColors['Clear'] +  BannerModify.GetBannerFromFile("main_screen")).encode())
    socket.send("                        Choose an option: ".encode())
    option_dude = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    # try:
    if int(option_dude) == 1:
        login(socket,addr)
    elif int(option_dude) == 2:
        register(socket,addr)
    # elif int(option_dude) == 3 or option_dude == "chatroom":
    #     ServerConfig.clients.append(["Guest" + str(random.randint(0, 99999)), socket, addr[0], addr[1]])
    #     WockyChat(socket, addr)
    # elif int(option_dude) == 4:
        # about(socket)
    else:
        socket.send("[x] Error, Wrong option!\r\n".encode())
        socket.close()
    # except:
    #     socket.send("[x] Error, You didnt choose a number!".encode())
    #     socket.close()


def login(socket, addr):
    if NetSettings.login == True:
        socket.send(str(Strings.MainColors['Clear']).encode())
        # User Input Login Section
        socket.send("\rUsername: ".encode())
        username = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
        if username == "" or username == None:
            username = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
        socket.recv(512)
        socket.send(str(f"\rPassword: {Strings.MainColors['Black']}").encode())
        password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")

        print(f"{username} | {password}") #Debugging

        # Login Check
        if "[+]" in Auth.Login(username, password, addr[0]): # This is a weird way of authentication lol 
            Strings.CurrentUser = username
            Strings.CurrentIP = addr[0]
            userinfo = CRUD
            socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + "\r\n").encode())
            socket.send(f"Welcome to Wocky {username}\r\n\x1b[37m╔═[\x1b[35m{Strings.CurrentUser}\x1b[37m@\x1b[35mWocky\x1b[37m]\r\n╚════➢\x1b[32m ".encode())
            MainLogger.Log(f"login: {username} | Time: {utils.CurrentDateTime()}", True)
            CurrentConn = ServerUtils.GetCurrentConn(socket)
            CurrnentAttackToggle = False
            if CurrentConn == 0 or CurrentConn == "0":
                CurrnentAttackToggle = True
            else:
                CurrnentAttackToggle = False
            ServerConfig.clients.append([username, socket, addr[0], addr[1], CurrnentAttackToggle])
        else:
            socket.send(f"{Strings.MainColors['Reset']}[x] Error, Incorrect username or password. Try again....".encode())
            time.sleep(4)
            socket.close()
    else:
        socket.send("[x] Error, Wocky NET login is currently disabled for maintenance, try again later....\r\n".encode())
        socket.close()

def register(socket, addr): ##) Function not finished
    socket.send("Username: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n","")
    socket.send("Password: ".encode())
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    # Current.CurrentInfo['Username'] = username



def free_mode(socket, ip):
    return ""

def about(socket):
    return ""