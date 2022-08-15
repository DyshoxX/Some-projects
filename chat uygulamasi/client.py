import socket
import time

host_name = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.connect((host_name,port))

print("Bağlantı sağlandı !! host ismi : {}:{}".format(host_name,port))

message = input("----> ")
print("server bekleniyor...")

while message != "cikis":
    internet_soketi.send(message.encode())
    gelen_veri = internet_soketi.recv(1024).decode()

    print("SERVER : "+gelen_veri)
    
    message = input("-----> ")
    print("server bekleniyor...")

internet_soketi.close()