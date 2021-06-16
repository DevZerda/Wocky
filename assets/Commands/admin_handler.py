import os, sys, time

from ..auth.crud import *
from ..auth.crudFunc import *
from ..banner_system.modify import *
from ..utils.main import *

def admin_command(socket, addr, data):
    if CrudFunctions.isReseller(Strings.GetCurrentUsername(socket)) or CrudFunctions.isAdmin(Strings.GetCurrentUsername(socket)) or CrudFunctions.isOwner(Strings.GetCurrentUsername(socket)):
        if len(data) > len("admin "):
            args = []
            if " " in data:
                args = data.split(" ")

            if len(args) == 0:
                socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + BannerModify.GetBannerFromFile("admin_help")).encode())
            elif args[1] == "add":
                CRUD.CreateUser(args[2], args[3])
            elif args[1] == "remove":
                CRUD.RemoveUser(args[2])
            elif args[1] == "update":
                CRUD.updateUser(args[2], args[3], args[4], args[5], args[6])
            elif args[1] == "resetip":
                # finishing later
                pass
            elif args[1] == "changepw":
                CrudFunctions.changePW(args[2], args[3])
            elif args[1] == "blockip":
                pass
            elif args[1] == "blacklistip":
                pass
            elif args[1] == "login":
                if args[2] == "on":
                    pass
                elif args[2] == "off":
                    pass
                else:
                    pass
            elif args[1] == "stresser":
                if args[2] == "on":
                    pass
                elif args[2] == "off":
                    pass
                else:
                    pass
            elif args[1] == "searchlogs":
                pass
            elif args[1] == "searchattacks":
                pass
            elif args[1] == "searchlogins":
                pass
            elif args[1] == "motd":
                pass
            elif args[1] == "boardcast": 
                pass
            elif args[1] == "announce":
                pass
            elif args[1] == "kick":
                pass
            elif args[1] == "freeze":
                pass
        else:
            lol = BannerModify.GetBannerFromFile("admin_help")
            socket.send(str(f"{lol}\r\n").encode())
    else:
        socket.send("[x] Error, you aren't admin to use this command!\r\n".encode())