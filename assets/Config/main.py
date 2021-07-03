import os, sys, time

from ..auth.main import *
from ..auth.crud import *

class NetSettings:
	login = True
	stresser = True

class ServerConfig:
	clients = []
	bots = []

class Strings:

	CurrentUser = ""
	CurrentIP = ""
	CurrentLvl = ""
	CurrentMtime = ""
	CurrentConn = ""
	CurrentAdmin = ""
	Cooldown = 60

	appInfo = {
		"appCreator": "Zerda",
		"appOwner": "Exo",
		"appDevs": "Zerda, Exo",
		"appAdmins": "Pressure",
		"appVersion": "1.00"
	}

	

	def hostname(name):
		addName = "Net"
		if name:
			addName = name
		
		host = "\r\x1b[33m[\x1b[31mQuantum\x1b[33m@\x1b[31m" + addName + "\x1b[33m]══► $ "
		return host

	MainColors = {
		"Red": "\x1b[31m",
		"Yellow": "\x1b[33m",
		"Blue": "\x1b[34m",
		"Purple": "\x1b[35m",
		"Green": "\x1b[32m",
		"Cyan": "\x1b[36m",
		"Black": "\x1b[30m",
		"Grey": "\x1b[37m",
		"White": "\x1b[37m",
		"Reset": "\x1b[39m",
		"Background_Black": "\x1b[40m",
		"Background_Red": "\x1b[41m",
		"Background_Green": "\x1b[42m",
		"Background_Yellow": "\x1b[43m",
		"Background_Blue": "\x1b[44m",
		"Background_Purple": "\x1b[45m",
		"Background_Cyan": "\x1b[46m",
		"Background_LightGrey": "\x1b[47m",
		"Background_DarkGrey": "\x1b[100m",
		"Background_LightRed": "\x1b[101m",
		"Background_LightGreen": "\x1b[102m",
		"Background_LightYellow": "\x1b[103m",
		"Background_Reset": "\x1b[49m",
		"Clear": "\033[2J\033[1;1H"
	}


	def show_all_clients():
		g = 0
		client_list = ""
		for u in ServerConfig.clients:
			client_list += str(f"Socket ID: {g} | Username: {u[0]}\r\n")
			g += 1
		return client_list

	def show_all_bots():
		h = 0
		bot_list = ""
		for u in ServerConfig.bots:
			bot_list += str(f"Socket ID: {h} | Device IP: {u[2]}\r\n")
			h += 1
		return bot_list


class ServerFunc:
	def setInfo(user):
		info = CRUD.GetUser(user).split(",")
		i = 0
		for usr in ServerConfig.clients:
			if usr[0] == user:
				usr[4] = info[3] #lvl
				usr[5] = info[4] #maxtime
				usr[6] = info[5] #con
				usr[7] = info[7] #admin