import os, sys, time

from ..Config.main import *

class dbLookup:
    def logs(user):
        logsDB = open("./assets/db/logs.db", "r").read()
        logs = logsDB.split("\n")

        logList = "ID |    Date          Time           Command\r\n______________________________________\r\n"
        show_list = Strings.MainColors['Purple'] + "ID |    Date          Time           Command\r\n______________________________________\r\n" + Strings.MainColors['Reset']
        start_here = len(logs)-10
        print(len(logs))
        print(logs)
        print(start_here)
        mylog_c = 0
        i = 0
        for log in logs:
            if len(log) > 5:
                if log.startswith(f"('{user}"):
                    if start_here == i or start_here > i:
                        fix = log.replace("('","").replace("')", "").split("','")
                        gang = fix[2].split(" ")
                        date = gang[0]
                        time = gang[1].split(".")[0]
                        show_list += f"{mylog_c}  | {date}\t     {time}\t {fix[1]}\r\n\r\n"
                        mylog_c+=1
                    else:
                        fix = log.replace("('","").replace("')", "").split("','")                        
                        fix[2] = fix[2].split(".")[0]
                        logList += f"{i}  | {fix[2]}\t {fix[1]}\r\n\r\n"
            i += 1
        return show_list

    def attacks(user):
        logsDB = open("./assets/db/attacks.db", "r").read()
        logs = logsDB.split("\n")

        logList = "ID |    Date          Time           Attack\r\n______________________________________\r\n"
        show_list = Strings.MainColors['Purple'] + "ID |    Date          Time           Attack\r\n______________________________________\r\n" + Strings.MainColors['Reset']
        start_here = len(logs)-10
        print(len(logs))
        print(logs)
        print(start_here)
        mylog_c = 0
        i = 0
        for log in logs:
            if len(log) > 5:
                if log.startswith(f"('{user}"):
                    if start_here == i or start_here > i:
                        fix = log.replace("('","").replace("')", "").split("','")
                        fix[2] = fix[2].split(".")[0]
                        show_list += f"{mylog_c}  | {fix[2]}\t {fix[1]}\r\n\r\n"
                        mylog_c+=1
                    else:
                        fix = log.replace("('","").replace("')", "").split("','")                        
                        fix[2] = fix[2].split(".")[0]
                        logList += f"{i}  | {fix[2]}\t {fix[1]}\r\n\r\n"
            i += 1
        return show_list

    def logins(user):
        logsDB = open("./assets/db/logins.db", "r").read()
        logs = logsDB.split("\n")

        logList = "ID |    Date          Time           Login\r\n______________________________________\r\n"
        show_list = Strings.MainColors['Purple'] + "ID |    Date          Time           Login\r\n______________________________________\r\n" + Strings.MainColors['Reset']
        start_here = len(logs)-10
        print(len(logs))
        print(logs)
        print(start_here)
        mylog_c = 0
        i = 0
        for log in logs:
            if len(log) > 5:
                if log.startswith(f"('{user}"):
                    if start_here == i or start_here > i:
                        fix = log.replace("('","").replace("')", "").split("','")
                        fix[2] = fix[2].split(".")[0]
                        show_list += f"{mylog_c}  | {fix[2]}\t {fix[1]}\r\n\r\n"
                        mylog_c+=1
                    else:
                        fix = log.replace("('","").replace("')", "").split("','")                        
                        fix[2] = fix[2].split(".")[0]
                        logList += f"{i}  | {fix[2]}\t {fix[1]}\r\n\r\n"
            i += 1
        return show_list