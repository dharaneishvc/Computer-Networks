from socket import *
serverName = 'localhost'
serverPort = 12560
clientSocket = socket(AF_INET,SOCK_DGRAM)
no = int(input("Enter Tot no of commands: "))
for i in range(no):
    print(i+1, end=": ")
    message = input('Input the <itemname>,<unitprice>,<quantity> :').encode()
    clientSocket.sendto(bytes(message),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    #print (int(modifiedMessage))
clientSocket.close()
