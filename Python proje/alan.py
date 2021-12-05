import socket
import time

host_ismi = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.connect((host_ismi, port)) 


print(f"bağlantı sağlandı!! {host_ismi} : {port} ")

mesaj = input("----::")
print("server bekleniyor..")

while mesaj != "cikis": 
    internet_soketi.send(mesaj.encode())
    gelen_veri = internet_soketi.recv(1024).decode()

    print("Alan : "+ gelen_veri)

    mesaj = input("----::")
    print("alan bekleniyor...")

internet_soketi.close()








