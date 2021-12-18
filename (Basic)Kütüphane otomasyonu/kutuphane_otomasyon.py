import sys

with open("kayit.txt","r+",encoding="utf-8") as f:
    kayitlar = f.readlines()

with open("kitap.txt","r+",encoding="utf-8") as f:
    kitaplar = f.readlines()

kayit = []
kitap = []

admin_name = "admin"
admin_psw = "1234"

class Kutuphane():
    def __init__(self):
        self.kayit = kayit
        self.kayitlar = kayitlar
        self.admin_name = admin_name
        self.admin_psw = admin_psw
        self.kitaplar = kitaplar
        self.kitap = kitap

    def ogrenci_ekle(self):
        ogrenci_ad = input("Kaydetmek istediğiniz Öğrenci Adı : ")
        ogrenci_no = input("Kaydetmek istediğiniz öğrenci no : ")

        if (ogrenci_ad in kayitlar) and (ogrenci_no in kayitlar):
            print("Eklemeye çalıştığınız öğrenci zaten sistemde kayıtlı!")
        else:
            self.kayit.append("öğrenci adı = " + ogrenci_ad+"\n")
            self.kayit.append("öğrenci no = " + ogrenci_no+"\n"+"\n")
            with open("kayit.txt","a",encoding="utf-8") as f:
                f.writelines(self.kayit)

    def kitap_ekle(self):
        kitap_name = input("Eklemek istediğiniz kitap adı : ")
        eklenme_tarihi = input("Eklenme tarihi : ")

        if (kitap_name not in self.kitaplar) and (eklenme_tarihi not in self.kitaplar):
            self.kitap.append("Kitap Adı : " + kitap_name+"\n")
            self.kitap.append("Eklenme Tarihi : " + eklenme_tarihi+"\n")
            with open("kitap.txt","a",encoding="utf-8") as f:
                f.writelines(self.kitap)

    def admin_giris(self):
        admin_kullanici_adi = input("Kullanıcı adı : ")
        admin_password = input("Şifre : ")

        if (admin_kullanici_adi == self.admin_name) and (admin_password == self.admin_psw):
            print("1 - kayıtları görüntüle\n2 - Kayıtlı kitapları görüntüle")
            secim = input("Seçiminiz : ")
            if secim == "1":
                with open("kayit.txt","r+",encoding="utf-8") as f:
                    kayitli_kullanicilar = f.readlines()
                for kullanici in kayitli_kullanicilar:
                    print(kullanici.strip())
            if secim == "2":
                with open("kitap.txt","r+",encoding="utf-8") as f:
                    kayitli_kitaplar = f.readlines()
                for kitap in kayitli_kitaplar:
                    print(kitap.strip())

kutuphane = Kutuphane()

def main_menu():
    print("""
Kütüphane otomasyonuna hoşgeldiniz!
1 - Öğrenci ekle
2 - Admin giriş
3 - Kitap ekle
4 - çıkış
""")
    choice = input("=> ")
    if choice == "1":
        kutuphane.ogrenci_ekle()      
    elif choice == "2":
        kutuphane.admin_giris()
    elif choice == "3":
        kutuphane.kitap_ekle()
    elif choice == "4":
        sys.exit()

main_menu()
input("İşlem tamamlandı!")
