# Modules
import os, sys, time

# Files

class CLI_Control:
    def set_Title(socket, msg):
        socket.send(str(f"\033]0;{msg}\007").encode())

    def set_TerminalSize(socket, r, c):
        socket.send(str(f"").encode())

class CLI_CursorControl:
    """
    Move cursor up once!
    """
    def MoveCursorUpOnce(socket):
        socket.send("".encode())

    """
    Move Cursor up the amount you choose
    PS: 0 is not an option!
    """
    def MoveCursorUp(socket, c):
        send.send(f"".encode())

    """
    Move Cursor down once
    """
    def MoveCursorDownOnce(socket):
        socket.send("".encode())

    """
    Move Cursor down the amount you choose
    PS: 0 is not an option!
    """
    def MoveCursorDown(socket, c):
        socket.send(f"".encode())