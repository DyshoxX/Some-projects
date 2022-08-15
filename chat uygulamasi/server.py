import socket
import time

host_name = "localhost"
port = 7777

internet_soketi = socket.socket()
internet_soketi.bind((host_name,port))
internet_soketi.listen(1)

connection, adress = internet_soketi.accept()

print(str(adress)+" bağlantı başarıyla sağlandı.")

while True:
    while True:
        try:
            gelen_veri = str(connection.recv(1024).decode())
            print("Client şunu yolladı : "+gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            connection, adress = internet_soketi.accept()
            print(str(adress)+"bağlantı başarıyla sağlandı.")
    if gelen_veri == "cikis":
        break
    else:
        message = input("----->")
        print("Client bekleniyor...")
        connection.send(message.encode())

connection.close()