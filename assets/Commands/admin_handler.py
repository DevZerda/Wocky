import os, sys, time, threading

from ..auth.crud import *
from ..auth.crudFunc import *
from ..auth.adminFunc import *
from ..banner_system.modify import *
from ..utils.main import *
from ..Config.main import *
from ..Config.functions import *
from ..api_attack_system.main import *

# Admin Commands
from .admin_boardcast import *

def admin_command(socket, addr, data):
    if CrudFunctions.isReseller(ServerUtils.GetCurrentUsername(socket)) or CrudFunctions.isAdmin(ServerUtils.GetCurrentUsername(socket)) or CrudFunctions.isOwner(ServerUtils.GetCurrentUsername(socket)):
        if len(data) > len("admin "):
            args = []
            if " " in data:
                args = data.split(" ")

            if len(args) == 0:
                socket.send(str(Strings.MainColors['Clear'] + CustomBannerMaker.CreateMOTD(utils.GetMOTD()) + BannerModify.GetBannerFromFile("main") + BannerModify.GetBannerFromFile("admin_help")).encode())
            elif args[1] == "userlist":
                socket.send(str(AdminFunc.show_all_users()).encode())
            elif args[1] == "add":
                CRUD.CreateUser(args[2], args[3])
            elif args[1] == "remove":
                CRUD.RemoveUser(args[2])
            elif args[1] == "update":
                CRUD.updateUser(args[2], args[3], args[4], args[5])
            elif args[1] == "resetip":
                # finishing later
                pass
            elif args[1] == "changepw":
                CrudFunctions.changePW(args[2], args[3])
            elif args[1] == "blockip": ## need to finish
                pass
            elif args[1] == "blacklistip": ## need to finish
                pass
            elif args[1] == "login":
                if args[2] == "on":
                    NetSettings.login = True
                    socket.send(f"[+] Successfully changed login status (Current status: {NetSettings.login})\r\n".encode())
                elif args[2] == "off":
                    NetSettings.login = False
                    socket.send(f"[+] Successfully changed login status (Current status: {NetSettings.login})\r\n".encode())
                else:
                    socket.send("[x] Error, Invalid argument\r\n".encode())
            elif args[1] == "stresser":
                if args[2] == "on":
                    NetSettings.stresser = True
                    socket.send(f"[+] Successfully changed stresser status (Current status: {NetSettings.stresser})\r\n".encode())
                elif args[2] == "off":
                    NetSettings.stresser = False
                    socket.send(f"[+] Successfully changed stresser status (Current status: {NetSettings.stresser})\r\n".encode())
                else:
                    socket.send("[x] Error, Invalid argument\r\n".encode())
            elif args[1] == "searchlogs": ## need to finish
                pass
            elif args[1] == "searchattacks": ## need to finish
                pass
            elif args[1] == "searchlogins": ## need to finish
                pass
            elif args[1] == "motd":
                newMOTD = data.replace(f"{args[0]} {args[1]} ", "")
                socket.send(str(utils.changeMOTD(newMOTD)).encode())
            elif args[1] == "boardcast":
                boardcastmsg = data.replace(f"{args[0]} {args[1]} {args[2]} ", "")
                threading.Thread(target=Boardcast, args=(socket, int(args[2]), boardcastmsg)).start()
            elif args[1] == "announce": ## need to finish
                pass
            elif args[1] == "kick":
                AdminFunc.kick_user(socket, data.split(" ")[2])
            elif args[1] == "freeze": ## need to finish
                pass
            elif args[1] == "apilist":
                socket.send(str(APICrud.listAPIs()).encode())
            elif args[1] == "addapi":
                pass
            elif args[1] == "rmapi":
                pass
            elif args[1] == "updateapi":
                pass
            elif args[1] == "change_cooldown":
                Strings.Cooldown = int(args[2])
                socket.send(f"[+] Cooldown successfully changed ({args[2]})\r\n".encode())
        else:
            lol = BannerModify.GetBannerFromFile("admin_help")
            socket.send(str(f"{lol}\r\n").encode())
    else:
        socket.send("[x] Error, you aren't admin to use this command!\r\n".encode())