#!/usr/bin/env python
import socket 
import argparse
import os

def argumments():
    parser = argparse.ArgumentParser(prog="Enable server", description="Create server to listening for any connection", epilog="-h")
    parser.add_argument("-ip", "--direction", help="Direction to enable server")
    parser.add_argument("-p", "--port", help="Port to reciv conections", type=int)
    args = parser.parse_args()
    return args

class Server:
    def __init__(self, ip, port):
        self.ServerIP = ip
        self.ServerPort = port

    def enableServer(self):
        try:
            self.oServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.oServer.bind((self.ServerIP, self.ServerPort))
            print(f"[+] Server create on {self.ServerIP} : {self.ServerPort}")
        except Exception:
            print(f"[!] Error to create server, messsage error: {Exception}")

    def startServer(self):
        try:
            self.oServer.listen(1000)
            print(f"[+] Server enable on {self.ServerIP} : {self.ServerPort}")
            self.Client, self.addClient = self.oServer.accept()
            print(f"[+] Connection accept from {self.addClient}")
        except:
            print(f"[!] Error to enable server on {self.ServerIP} : {self.ServerPort}")
    
    def sendCommand(self):
        try:
            while True:
                cmd = input("$: ")
                if cmd == "clear" or "cls":
                    os.system("cls")
                cmd = cmd.encode("utf-8")
                self.Client.send(cmd)
                output = self.Client.recv(1024)
                print(output.decode("utf-8"))
        except:
            print(f"[!] Could not establish a command conection")
        

def main():
    args = argumments()
    oServer = Server(str(args.direction), args.port)
    oServer.enableServer()
    oServer.startServer()
    oServer.sendCommand()


if __name__ == '__main__':
    main()