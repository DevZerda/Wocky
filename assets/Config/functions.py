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