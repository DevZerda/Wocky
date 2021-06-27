from assets.banner_system.modify import BannerFunc
import os, sys, time

from ..Config.main import *
from ..utils.main import *
from ..banner_system.modify import *

def Boardcast(socket, boardtime, msg):
    if isinstance(boardtime, int):
        for usr in ServerConfig.clients:
                usr[1].send(str(f"\x1b]0;{msg}\007").encode())

        socket.send("[+] Successfully sent boardcast message!\r\n".encode())
        for i in range(0, int(boardtime)):
            time.sleep(1)

        socket.send("[+] Boardcast messaged successfully finished!".encode())
        for usr in ServerConfig.clients:
                CurrentT = utils.GetTitle()
                usr[1].send(str(f"\x1b]0;{BannerFunc.ColorBanner(CurrentT)}\007").encode())
    else:
        socket.send(f"[x] Error, Invalid time was provided!\r\n".encode())