import os, sys, time

from .crud import *
from .crudFunc import *
from ..Config.main import *


class AdminFunc:
    def show_all_users():
        userline = ""
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")
        userline += "Username      IP         Level   Maxtime Conn  On-Going  Admin\r\n_____________________________________________________________________\r\n"
        for user in users:
            if len(user) > 5:
                fix = user.replace("('", "").replace("')", "").replace("','", ",")
                fix2 = user.replace("('", "").replace("')", "").split("','")
                userline += f"{fix2[0]}\t     {fix2[1]}\t  {fix2[3]}\t   {fix2[4]}\t   {fix2[5]}\t   {fix2[6]}\t   {fix2[7]}\r\n"
                # print(fix)
        return userline

    def kick_user(socket, user):
        # try:
        print(f"{ServerConfig.clients[int(user)]}\r\n")
        if socket == ServerConfig.clients[int(user)][1]:
            socket.send("[x] Error, You cannot kick yourself dummy!\r\n".encode())
        else:
            try:
                ServerConfig.clients[int(user)][1].send(str(f"{Strings.MainColors['Clear']} {Strings.MainColors['Red']}\r\n\r\n\r\n\r\nYou just got kick by an admin!").encode())
                ServerConfig.clients[int(user)][1].close()
            except:
                socket.send(str(f"[x] Error, Failed to kick user!\r\n").encode())

            try:
                ServerConfig.clients.pop(int(user))
            except:
                socket.send("[x] Error, Unable to remove element from array".encode())

            socket.send(str(f"[+] User: {user} successfully kicked from the net!\r\n").encode())
        # except:
            # socket.send(str(f"[x] Error, Failed to kick user!\r\n").encode())

    def boardcastmsg(socket, msg):
        for usr in ServerConfig.clients:
            if usr[1] != socket:
                usr[1].send(str(f"\r\n[NEW MESSAGE FROM ADMIN]\r\n{msg}\r\n[~]════[Wocky]══$ ").encode())
        socket.send("[+] Boardcast message successfully sent!\r\n".encode())


        