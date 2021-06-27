# from Quantum_setup import GetOS
import os, sys, time, platform, datetime

class utils:
    def set_Title(socket, msg):
        socket.send(f"\033]0;{msg}\007".encode())

    def CurrentDateTime(): # This is date and time not just time !
        now = datetime.datetime.now()
        return now

    def FlashingCursor(socket):
        while(True):
            socket.send("\033[?25l".encode())
            time.sleep(1)
            socket.send("\033[?25h\033[?0c".encode())
            time.sleep(1)

    def changeMOTD(new_motd):
        motd = open("./assets/db/motd.db", "w")
        motd.write(new_motd)
        motd.close()
        return f"MOTD Successfully changed to ({new_motd})"

    def GetMOTD():
        motd = open("./assets/db/motd.db", "r").read()
        return motd

    def changeTitle(newT):
        w_title = open("./assets/db/wocky_title.db", "w")
        w_title.write(newT)
        w_title.close()
        return "[+] Title successfully changed!\r\n"

    def GetTitle():
        title = open("./assets/db/wocky_title.db", "r").read()
        return title


class OS_Func:
    def GetOSType():
        if "Windows" in platform.platform():
            return False
        elif "Linux" in platform.platform():
            return True
        else:
            print("[x] Error, This net does not support this OS")
            exit()

class arrUtils:
    def arr2str(arr, between):
        if isinstance(arr, list) == False:
            print("[x] Error, Invalid value provided!")
            exit(0)
        n_str = ""
        for u in arr:
            n_str += u + between

        return n_str

