import os, sys, time

from ..Config.main import *

buffer_length = 1024


def WockyChat(socket, addr):
    socket.send(str(f"Welcome to wocky chat: {Strings.GetCurrentUsername(socket)}!").encode())
    while(True):
        msg = socket.recv(buffer_length).decode().strip().replace("\r\n", "\n").replace("\n", "")
        if msg == "exit":
            return
        else:
            for u in ServerConfig.clients:
                if u[1] != socket:
                    u[1].send(str(msg).encode())