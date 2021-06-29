import requests, sys, json

def mtr(socket, argv):
    if len(argv) == 2:
        jsonResp = (requests.get("https://api.hackertarget.com/mtr/?q=" + argv[1]).text)
        sanitize = jsonResp.replace("\",\"", "\r\n")
        sanitize = sanitize.replace("\"", "").replace("{", "").replace("}", "")
        socket.send(f"{sanitize}\r\n".encode(""))
    else:
        socket.send("[x] Error, Invalid Arugment\r\nUsage: dns <URL>\r\n".encode())