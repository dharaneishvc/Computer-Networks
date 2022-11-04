dicinv = {
  "Apple": 120,
  "Orange": 150,
  "Guava": 140,
  "Graphes": 150,
  "Mango": 135
}

def showdet():
    print("Inventary Details:")
    for a in dicinv.keys():
        print(a, ":", dicinv[a])
from socket import *
serverPort = 12560
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))
print ("The server is ready to receive")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    message = str(message)
    if(message[2:-1]=="Records"):
        showdet()
        cos = 0;
        serverSocket.sendto(bytes(cos), clientAddress)
    else:
        cos = 0;
        a = message[2:-1].split(",")
        print(a, type(a), message)
        if a[1].isnumeric() and a[2].isnumeric() and dicinv[a[0]]>int(a[1]):
            dicinv[a[0]] -= int(a[1])
            cos += int(a[1])*int(a[2]);
        else:
            print("Error")
        print("Tot:", cos);
        showdet()
        cos = bytes(cos)
        serverSocket.sendto(cos, clientAddress)
