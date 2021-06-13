import os, sys, time

buffer_length = 1024

def CMDHandler(socket, addr):
    socket.send(str("╔══════[Wocky]══[~]\r\n╚═══ $ ").encode())
    data = str(socket.recv(buffer_length).decode()).strip().replace("\r\n", "")

    print(data)
    if data.lower() == "help" or data.lower() == "?":
        socket.send("gang".encode())