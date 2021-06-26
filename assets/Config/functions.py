import os, sys, time

from .main import *

class ServerUtils:
	def GetCurrentUsername(socket):
		for u in ServerConfig.clients:
			if u[1] == socket:
				return u[0]

		return "[x] Failed!"

	def GetCurrentIP(socket):
		for u in ServerConfig.clients:
			if u[1] == socket:
				return u[2]

		return "[x] Failed!"

	def GetCurrentLvl(socket):
		for u in ServerConfig.clients:
			if u[1] == socket:
				return u[4]

		return "[x] Failed!"

	def GetCurrentMaxtime(socket):
		for u in ServerConfig.clients:
			if u[1] == socket:
				return u[5]

		return "[x] Failed!"

	def GetCurrentConn(socket):
		for u in ServerConfig.clients:
			if u[1] == socket:
				return u[6]

		return "[x] Failed!"
		
	def GetCurrentAdmin(socket):
		for u in ServerConfig.clients:
			if u[1] == socket:
				return u[7]

		return "[x] Failed!"