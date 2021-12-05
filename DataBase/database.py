import time

admin = "yourgm@gmail.com"
sifre = "123456"


def kayit():
    email = str(input("E mailinizi giriniz : "))
    password = str(input("Parolanızı giriniz : "))
    repeat_password = str(input("Parolanızı tekrar giriniz : "))
    if password == repeat_password:
        with open("kayit.txt","a",encoding="utf-8") as file:
            bosluk = "\n"
            file.write(bosluk)
            file.write(email)
            file.write(bosluk)
            file.write(password)
            file.write(bosluk)


def giris():
    email = str(input("E mailinizi giriniz : "))
    password = str(input("Parolanızı giriniz : "))

    if email == admin and password == sifre:
        with open("kayit.txt","r",encoding="utf-8") as file:
            print(file.read())
            input("-"*50)


while True:
    opsiyon = int(input("[1]Kayıt\n[2]Admin Giriş\n[3]Çıkış\n=>  "))
    if opsiyon == 1:
        time.sleep(1)
        kayit()
        print("-"*50)
    elif opsiyon == 2:
        time.sleep(1)
        giris()
        print("-"*50)
    elif opsiyon == 3:
        break

