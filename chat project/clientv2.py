import socket

host = "localhost" #bağlanacağımız host
port = 7777 #bağlanacağımız port

socket = socket.socket() #işlem yapmak için soket oluşturduk
socket.connect((host,port)) #belirtilen host ipdeki porta bağlandık

print(f"Bağlantı sağlandı {host}:{port}") #belirtilen hosta bağlanıldığını belirtir.

message = input("----->>") #gönderilecek mesaj
print("server bekleniyor...")

while message != "cikis":
    socket.send(message.encode()) #gönderilecek mesajımızı encodeile şifreler ve gönderir
    gelen_veri = socket.recv(1024).decode() #karşıdan gelen mesajın şifresini çözer

    print("SERVER : "+gelen_veri) #akrşıdan gelen mesajı yazdırır ekrana.

    message = input("---->>>") #mesaj geldikten sonra gönderilecek mesajı alır
    print("server bekleniyor...")

socket.close() #bağlantıyı kapattık.