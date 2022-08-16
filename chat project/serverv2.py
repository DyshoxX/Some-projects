import socket
import time

host = "localhost"
port = 7777

socket = socket.socket() #host:port şeklinde soketi oluşturdum
socket.bind((host,port)) #soketi işleme tabi tutacak şekilde dahil ettim
socket.listen(1) #soketi dinlemeye aldım parantez içindeki sayı kaç kişiyi dinleyebileceği

connection, adress = socket.accept() #uygulamayı bağlantı gelinceye kadar bekler ve verileri alır
print(str(adress)+" Bağlantı başarıyla sağlandı.") #bağlantının sağlandığını belirtir

while True: #if else şart bloklarının çalışacağı ana çatıyı oluşturduk mesajı alacak sürekli
    while True :#try except bloklarının çalışacağı döngü yapısını kurdum
        try:
            gelen_veri = str(connection.recv(1024).decode()) #karşı bağlantıdan gelen veriyi stringe çevirir okunur hale getirir.
            print("Client yolladı : "+gelen_veri) #karşı bağlantıdan gelen veriyi yazdırır.
            break
        except ConnectionResetError: #hata olursa bağlantıyı 2saniye sonra tekrar kurar 
            time.sleep(2)
            connection, adress = socket.accept()
            print(str(adress)+" Bağlantı başarıyla sağlandı.")
    if gelen_veri == "cikis":
        break
    else:
        message = input("----->>>") # #karşı kullanıcıya gidecek mesajı alır.
        print("Client bekleniyor...")
        connection.send(message.encode()) #karşı kullanıcıya gidecek mesajı encode ile şifreler yollar 

connection.close() #bağlantıyı kapatır.