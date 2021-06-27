import os, sys, time
from ..Config.main import *
from .functions import *

banner = """                              Official Wocky NET
   
     [Zerda]             !~  Welcome To Wocky NET ~!                [v1.00]
     - Official bot testing CNC
     _______________________________________________________________
         COMMANDS               USAGE               DESCRIPTION
         
         - kick                 kick <SID>          kick bot
         - cmd                  cmd <cmd>           send a cmd to server
         - bots                 bots                list of bots
         - clear                c                   clear screen
"""
cp_hostname = "Wocky >> "

def CP():
    print(banner)
    while(True):
        inputCMD = input(cp_hostname)
        if inputCMD == "bots":
            show_all_bots()
        elif inputCMD == "users":
            show_all_clients()
        elif inputCMD == "c":
            os.system("clear")
            print(banner)