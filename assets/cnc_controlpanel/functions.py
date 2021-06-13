import os, sys, time

from ..Config.main import *

def show_all_bots():
    bot_c = 0 
    for bot in ServerConfig.bots:
        print(f"Socket ID: {bot_c} | System IP: {bot[2]} | System Port: {bot[3]}")
        bot_c += 1

def show_all_clients():
    client_c = 0
    for client in ServerConfig.clients:
        print(f"Socket ID: {client_c} | Client Name: {client[0]} | Client IP: {client[2]}")
        client_c += 1