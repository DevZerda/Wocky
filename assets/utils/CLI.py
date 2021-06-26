# Modules
import os, sys, time

# Files

# this file isnt done u gonna add more lol ! yh

class CLI_Control:
    def set_Title(socket, msg):
        socket.send(str(f"\033]0;{msg}\007").encode())

    def set_TerminalSize(socket, r, c):
        socket.send(str(f"\033[8;{r};{c}t").encode())

class CLI_CursorControl:
    """
    Set cursor at a certain position on the current CLI
    """
    def setCursorPosition(socket, r, c):
        socket.send(f"\033[{r};{c}f".encode())

    """
    Move cursor to a different line
    PS. 0 is not an option
    """
    def setCursorToLine(socket, r):
        socket.send(f"\033[{r};0f".encode())

    def setCursorToColumn(socket, c):
        socket.send(f"\033[0;{c}f".encode())

    """
    Move cursor up once!
    """
    def MoveCursorUpOnce(socket):
        socket.send("\033[1A".encode())

    """
    Move Cursor up the amount you choose
    PS: 0 is not an option!
    """
    def MoveCursorUp(socket, c):
        send.send(f"\033[{c}A".encode())

    """
    Move Cursor down once
    """
    def MoveCursorDownOnce(socket):
        socket.send("\033[1B".encode())

    """
    Move Cursor down by choice
    PS: 0 is not an option!
    """
    def MoveCursorDown(socket, c):
        socket.send(f"\033[{c}B".encode())

    """
    Move Cursor left once
    """
    def MoveCursorLeftOnce(socket):
        socket.send("\033[1D".encode())

    """
    Move Cursor left by choice
    PS: 0 is not an option
    """
    def MoveCursorLeft(socket, c):
        socket.send(f"\033[{c}D".encode())

    """
    Move Cursor right once
    """
    def MoveCursorRightOnce(socket):
        socket.send("\033[1C".encode())

    """
    
    """
    def MoveCursorRight(socket, c):
        socket.send(f"\033[{c}C".encode())


class CLI_EraserControl:
    def HideCursor(socket):
        socket.send("\033[?251".encode())

    def ShowCursor(socket):
        socket.send("\033[?25h\033[?0c".encode())


def FlashCursor(socket):
    i = 0
    while(True):
        CLI_EraserControl.HideCursor(socket)
        time.sleep(2)
        CLI_EraserControl.ShowCursor(socket)
        if i == 10:
            return
        i+=1