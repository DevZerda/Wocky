import os, sys, time, subprocess

class CRUD:
    def GetUser(Finduser):
        try:
            db = open("./assets/db/users.db", "r").read()
            users = db.split("\n")

            user_found = False
            user_line = ""

            for user in users:
                # print(user) #Debugging
                if len(user) > 4:
                    if user.startswith("('" + Finduser):
                        user_found = True
                        new = user.replace("('", "")
                        new1 = new.replace("')", "")
                        user_line = new1.replace("','", ",")
        
            if user_found:
                return user_line
            else:
                return "[x] Error, No user found!"
        except:
            print("File: /assets/auth/crud.py | Line: 4 | Function: GetUser(user)\r\n[x] Unable to find database file!\r\n")
            exit()

    def CreateUser(user, password, level, maxtime, admin):
        try:
            if f"('{user}" in open("./assets/db/users.db", "r").read():
                return f"[x] User: {user} is already taken, choose another username!"

            db = open("./assets/db/users.db", "a")
            db.write(f"('{user}','none','{password}','{level}','{maxtime}','{admin}')\n")
            db.close()
            return f"[+] User: {user} successfully added!\r\n"
        except:
            print("File: /assets/auth/crud.py | Line: 29 | Function: CreateUser(user, password, level, maxtime, admin)\r\n[x] Unable to find database file!\r\n")
            exit()
    
    def RemoveUser(user):
        try:
            db = open("./assets/db/users.db", "r").read()
            users = db.split("\n")

            new_db = ""

            for u in users:
                if len(u) > 4:
                    if user in u:
                        ## Edit user here
                        print("User found and removed!")
                    else:
                        new_db += u + "\n"

            w_db = open("./assets/db/users.db", "w")
            w_db.write(new_db)
            w_db.close()
            return f"[x] User: {user} successfully updated!\r\n"
        except:
            print("File: /assets/auth/crud.py | Line: 39 | Function: RemoveUser(user)\r\n[x] Error, Unable to find database file!\r\n")
            exit()

    def updateUser(user, newlvl, newmtime, newadmin):
        try:
            db = open("./assets/db/users.db", "r").read()
            users = db.split("\n")

            new_db = ""

            for usr in users:
                if len(usr) > 5:
                    if usr.startswith("('" + usr):
                        fix = usr.replace("('", "")
                        fix2 = fix.replace("')", "")
                        userinfo = fix2.split("','")
                        new_db += "('" + userinfo[0] + "','" + userinfo[1] + "','" + userinfo[2] + "','" + newlvl + "','" + newmtime + "','" + newadmin + "')\n"
                    else:
                        new_db += usr

            w_db = open("./assets/db/users.db", "w")
            w_db.write(new_db)
            return f"User: {user} successfully updated!\r\n"
        except:
            print("File: /assets/auth/crud.py | Line: 62 | Function updateUser(user, newlvl, newmtime, newadmin)\r\n[x] Error, Unable to find database file!\r\n")
            exit()

    def CreateRegisterToken(level, time, admin):
        try:
            tokenDB = open("./assets/db/tokens.db", "a")
            new_token = subprocess.getoutput("tr -dc A-Za-z0-9 </dev/urandom | head -c 45 ; echo ''")
            tokenDB.write(f"token={new_token},level={level},time={time},admin={admin}")
            tokenDB.close()
            return f"Token generated: {new_token}\r\n"
        except:
            print("File: /assets/auth/crud.py | Line: 86 | Function: CreateRegisterToken(level, time, admin)\r\n[x] Error, Unable to find token database file!\r\n")
            exit()

        
    def GetTokenInfo(rtoken):
        try:
            tokenDB = open("./assets/db/tokens.db", "r").read()
            tokens = tokenDB.split("\n")

            for token in tokens:
                if len(token) > 4:
                    if rtoken in token:
                        return rtoken

            return False
        except:
            print("File: /assets/auth/crud.py | Line: 98 | Function: GetTokenInfo(rtoken)\r\n[x] Error, Unable to find tokan database file!\r\n")
            exit()