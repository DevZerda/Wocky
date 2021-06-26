import os, sys, time

from ..Config.main import *
from ..Config.functions import *
from ..banner_system.modify import *

def msg_user(socket, data):
    msg = data.split(" ")
    CurrentUser = ServerUtils.GetCurrentUsername(socket)
    sendMsg = data.replace(f"{msg[0]} {msg[1]} ", "")
    for user in ServerConfig.clients:
        if user[0] == msg[1]:
            user[1].send(f"\r\n[Message From: {CurrentUser}]\r\nMessage: {BannerFunc.ColorBanner(sendMsg)}\r\n[~]════[Wocky]══$ ".encode())