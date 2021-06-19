import os, sys, time

from ..Config.main import *
from ..Config.functions import *

def msg_user(socket, data):
    msg = data.split(" ")
    sendMsg = data.replace(f"{data[0]} {data[1]}", "")
    CurrentUser = ServerUtils.GetCurrentUsername(socket)
    for user in ServerConfig.clients:
        if user[0] == msg[1]:
            user[1].send(f"\r\n[Message From]\r\n{CurrentUser}: {sendMsg}\r\n[~]════[Wocky]══$ ".encode())