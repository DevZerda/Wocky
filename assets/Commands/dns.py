import requests, json, sys

def dns(socket, argv):
    if len(argv) == 2:
        jsonResp = (requests.get("https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=dns&string=" + argv[1]).text)
        sanitize = jsonResp.replace("\",\"", "\r\n")
        sanitize = sanitize.replace("\"", "").replace("{", "").replace("}", "")
        socket.send(f"{sanitize}\r\n".encode(""))
    else:
        socket.send("[x] Error, Invalid Arugment\r\nUsage: dns <URL>\r\n".encode())
