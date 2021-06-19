import os, sys, time

from .crud import *
from .crudFunc import *
from ..Config.main import *


class AdminFunc:
    def show_all_users():
        userline = ""
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")
        userline += "Username    IP   Level   Maxtime Conn  On-Going  Admin\r\n_____________________________________________________________________\r\n"
        for user in users:
            if len(user) > 5:
                fix = user.replace("('", "").replace("')", "").replace("','", ",")
                fix2 = user.replace("('", "").replace("')", "").split("','")
                userline += f"{fix2[0]}\t   {fix2[1]}\t   {fix2[3]}\t   {fix2[4]}\t   {fix2[5]}\t   {fix2[6]}\t   {fix2[7]}\r\n"
                # print(fix)
        return userline

    def kick_user(socket, user):
        f = 0
        for u in ServerConfig.clients:
            if u[0] == user:
                u[1].send(str(Strings.MainColors['Clear'] + Strings.MainColors['Red'] + "\r\n\r\n\r\n\r\n\r\n\r\nYou have been disconnected by an admin!").encode())
                time.sleep(5)
                u[1].close()
                ServerConfig.clients[f].pop()
                return f"[+] User: {user} successfully kicked from the net!\r\n"
            f += 1
        return f"[x] Error, Failed to kick user!\r\n"
        