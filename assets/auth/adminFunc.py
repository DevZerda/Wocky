import os, sys, time

from .crud import *
from .crudFunc import *


class AdminFunc:
    def show_all_users():
        db = open("./assets/db/users.db", "r").read()
        users = db.split("\n")

        print("Option 1\t Option 2\t   Option 3\t   Option 4\t   Option 5\t   Option 6")
        for user in users:
            if len(user) > 5:
                fix = user.replace("('", "").replace("')", "").replace("','", ",")
                fix2 = user.replace("('", "").replace("')", "").split("','")
                print(f"{fix2[0]}\t {fix2[1]}\t {fix2[3]}\t {fix2[4]}\t {fix2[5]}\t {fix2[6]}\t {fix2[7]}")
                # print(fix)

        