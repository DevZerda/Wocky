# Modules
import os, sys, time, random

# Files
from ..auth.main import *
from ..Logger.main import *
from ..banner_system.modify import *
from ..Config.main import *
from .chatroom import *

buffer_length = 1024

def MainScreen(socket, addr):
    socket.send(str(Strings.MainColors['Clear'] +  BannerModify.GetBannerFromFile("main_screen")).encode())
    socket.send("                        Choose an option: ".encode())
    option_dude = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    if int(option_dude) == 1:
        login(socket,addr)
    elif int(option_dude) == 2:
        register(socket,addr)
    elif int(option_dude) == 3:
        ServerConfig.clients.append(["Guest" + str(random.randint(0, 99999)), socket, addr[0], addr[1]])
        WockyChat(socket, addr)
    elif int(option_dude) == 4:
        about(socket)
    else:
        socket.send("[x] Error, Invalid Argument\r\n".encode())
        MainScreen(socket,addr)



def login(socket, addr):
    socket.send(str(Strings.MainColors['Clear']).encode())
    # User Input Login Section
    socket.send("\rUsername: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    socket.recv(512)
    socket.send("\rPassword: ".encode())
    socket.recv(512)
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")

    print(f"{username} | {password}") #Debugging

    # Login Check
    if "[+]" in Auth.Login(username, password, addr[0]): # This is a weird way of authentication lol 
        Strings.CurrentUser = username
        Strings.CurrentIP = addr[0]
        socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + "\r\n").encode())
        socket.send(f"Welcome to Quantum Net {username}\r\n".encode())
        MainLogger.Log(f"login: {username} | Time: {utils.CurrentTime()}", True)
        ServerConfig.clients.append([username, socket, addr[0], addr[1]])
    else:
        socket.send("[x] Error, Incorrect username or password. Try again....".encode())
        time.sleep(4)
        socket.close()

def register(socket, addr): ##) Function not finished
    socket.send("Username: ".encode())
    username = socket.recv(buffer_length).decode().strip().replace("\r\n","")
    socket.send("Password: ".encode())
    password = socket.recv(buffer_length).decode().strip().replace("\r\n", "")
    Current.CurrentInfo['Username'] = username



def free_mode(socket, ip):
    return ""

def about(socket):
    return ""