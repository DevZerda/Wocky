import os, sys, time

from ..Config.main import *

class db_Stats:
    def TotalUsers():
        db = len((open("./assets/db/users.db", "r").read()).split("\n"))
        return db-1

    def OnlineUsers():
        db = len(ServerConfig.clients)
        return db

    def TotalAttack():
        db = len((open("./assets/db/attacks.db", "r").read()).split("\n"))
        return db-1