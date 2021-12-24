import sys
import random

class MP3calar():
    sarkilar = []
    ses_seviyesi = 0
    calinan_sarki = ""
    def __init__(self):
        self.sarkilar = MP3calar.sarkilar
        self.ses_seviyesi = MP3calar.ses_seviyesi
        self.calinan_sarki = MP3calar.calinan_sarki
    
    def sarkiSec(self):
        calinan_sarki = random.choice(self.sarkilar)
        return calinan_sarki

    def sarkiEkle(self):
        sarki = input("Şarkı adı: ")
        self.sarkilar.append(sarki)

    def sarkiSil(self):
        sarki = input("Şarkı adı: ")
        self.sarkilar.remove(sarki)

    def sesArttir(self):
        if self.ses_seviyesi < 100:
            self.ses_seviyesi = self.ses_seviyesi + 10
            print(self.ses_seviyesi)
            return self.ses_seviyesi
        else:
            print("Zaten maksimum ses seviyesindesiniz! ")

    def sesAzalt(self):
        if self.ses_seviyesi >= 10:
            self.ses_seviyesi = self.ses_seviyesi - 10
            print(self.ses_seviyesi)
            return self.ses_seviyesi
        else:
            print("Ses seviyesi minimum 10 olabilir! ")

    def rastgeleSarkiSec(self):
        rSarki = random.choice(self.sarkilar)
        print(f"{len(self.sarkilar)} şarkı arasından seçilen şarkı : {rSarki}")

    def kapa(self):
        sys.exit()

def main():
    mp3 = MP3calar()
    print(f"Şarkı listesi:{mp3.sarkilar}\nŞuan çalınan şarkı: \nSes : {mp3.ses_seviyesi}\n\n1 - Şarkı seç\n2 - Ses arttır\n3 - Ses azalt\n4 - Rastgele şarkı seç\n5 - Şarkı ekle\n6 - Şarkı sil\n7 - Çıkış ")
    secim = input("Seçiminiz : ")
    if secim == "1":
        mp3.sarkiSec()
    elif secim == "2":
       mp3.sesArttir()
    elif secim == "3":
        mp3.sesAzalt()
    elif secim == "4":
        mp3.rastgeleSarkiSec()
    elif secim == "5":
        mp3.sarkiEkle()
    elif secim == "6":
        mp3.sarkiSil()
    elif secim == "7":
        mp3.kapa()

main()
while True:
    option = input("Devam etmek istiyor musunuz? (e/h) : ")
    if option == "e":
        main()
    elif option == "h":
        break
    else:
        break