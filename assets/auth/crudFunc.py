import os, sys, time
from .crud import *

class CrudFunctions:
    def MyStats(user):
        info = CRUD.GetUser(user).split(",")
        r = f"User: {info[0]}\n"
        r += f"IP: {info[1]}\n"
        r += f"Level: {info[3]}\n"
        r += f"Maxtime: {info[4]}\n"
        r += f"Concurrents: {info[5]}\n"
        r += f"On-going: {info[6]}\n"
        r += f"Admin: {info[7]}\n"
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
    # ('root','none','niggered','2','1200','2','2')
    #     0     1        2       3     4    5   6
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
