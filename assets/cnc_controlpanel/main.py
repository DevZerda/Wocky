import os, sys, time
from ..Config.main import *
from .functions import *

banner = r"""   ╔════════════════════════════════════════════════════════════════════════╗
   ║                          Official Wocky NET                            ║
   ╠════════════════════════════════════════════════════════════════════════╣
   ║ [Ashlee]            !~  Welcome To Wocky NET ~!                [v1.00] ║
   ║ - Official bot testing CNC                                             ║
   ║ _______________________________________________________________        ║
   ║     COMMANDS               USAGE               DESCRIPTION             ║
   ║     - kick                 kick <SID>          kick bot                ║
   ║     - cmd                  cmd <cmd>           send a cmd to server    ║
   ║     - bots                 bots                list of bots            ║
   ║     - clear                c                   clear screen            ║
   ╚════════════════════════════════════════════════════════════════════════╝

   """
cp_hostname = "QuantumCP >> "

def CP():
    while(True):
        inputCMD = input(cp_hostname)
        if inputCMD == "bots":
            show_all_bots()