import time

with open("kullanicilar.txt","r+") as kullanicilar:
    users = kullanicilar.readlines()

class User():
    def __init__(self):
        self.users = users

    def login(self):
        username = input("Kullanici adı : ")
        password = input("Şifre : ")

        kisiler = []
        for kisi in self.users:
            kisiler.append(kisi.strip())
        
        if (username in kisiler) and (password in kisiler):
            print("Giriş başarılı!")
        else:
            print("Parola veya kullanıcı adı hatalı lütfen tekrar deneyiniz!")

    def register(self):
        kAdi = input("Kullanıcı adı : ")
        sifre = input("Şifre : ")
        
        with open("kullanicilar.txt","a") as file:
            file.write(kAdi+"\n")
            file.write(sifre+"\n"+"\n")

        print("Kullanıcı başarıyla oluşturuldu!")

    def main_menu(self):
        menu = User()
        secim = input("Yapmak işediğiniz işlem:\n[1]Login\n[2]Register\n ==> ")
        if secim == "1":
            print("Seçim bekleniyor...")
            time.sleep(1)
            menu.login()
        elif secim == "2":
            print("Seçim bekleniyor...")
            time.sleep(1)
            menu.register()
        else:
            print("Seçiminizi kontrol ediniz!")

ornek = User()
ornek.main_menu()