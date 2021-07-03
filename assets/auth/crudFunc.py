import os, sys, time
from .crud import *

class CrudFunctions:
    def MyStats(user):
        info = CRUD.GetUser(user).split(",")
        r = f"User: {info[0]}\r\n"
        r += f"IP: {info[1]}\r\n"
        r += f"Level: {info[3]}\r\n"
        r += f"Maxtime: {info[4]}\r\n"
        r += f"Concurrents: {info[5]}\r\n"
        r += f"On-going: {info[6]}\r\n"
        r += f"Admin: {info[7]}\r\n"
        return r


    def TokenValidation(rtoken):
        return ""
        
    def ChangePW(user, newpw):
        info = CRUD.GetUser(user).split(",")
        CRUD.RemoveUser(user)
        CRUD.CreateUser(info[0], newpw, info[3], info[4], info[5])
        return "Password successfully changed!\r\n"

    def isRegistered(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return False

        return True
    
    def isPremium(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[3]) == 0:
            return False
        elif int(info[3]) > 0 & int(info[3]) <= 5:
            return True
        else:
            return False

    def isReseller(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[7]) == 1:
            return True
        else:
            return False
    #   user    ip      pw    lvl mtime  conn ongoing admin expiry
    # ('root','none','lulzsec','2','1200','2','0','2','0/0/0')
    #     0     1        2       3     4   5   6   7    8
    def isAdmin(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[7]) == 2:
            return True
        else:
            return False

    def isOwner(username):
        info = CRUD.GetUser(username)
        if info == "[x] Error, No user found!":
            return "[x] Error, No user found!\r\n (This seems like a buggy function)"

        info = info.split(",")
        if int(info[7]) == 3:
            return True
        else:
            return False
    
    def AttackValidation(user):
        UserInfo = CRUD.GetUser(user)
        if "[x]" in UserInfo:
            return False

        InfoArr = UserInfo.split(",")
        if int(InfoArr[6]) == int(InfoArr[5]):
            return False
        else:
            return True

    def DownOneConn(user):
        ## fuck me 
        pass
