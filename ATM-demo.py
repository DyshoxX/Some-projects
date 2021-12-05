anlik_para = 0
bakiye = {"hesapName" : anlik_para}
    
def kayit_yap():
    kayit_kullanici_adi = str(input("Sistemde Kayıtlı Olmayan Kullanıcı Adınızı Giriniz : "))
    kayit_psw = str(input("Şifrenizi giriniz : "))
    kayit_psw_tekrar = str(input("Şifrenizi tekrar giriniz : "))
    bosluk = "\n"
    with open("C:/Users/kadir/Desktop/kullaniciler.txt","r+",encoding="utf-8") as file:
        if kayit_kullanici_adi not in file.read():
            if kayit_psw == kayit_psw_tekrar:
                file.write(bosluk)
                file.write(kayit_kullanici_adi)
                file.write(bosluk)
                file.write(kayit_psw)
                file.write(bosluk)
            else:
                pass
        else:
            print("HATA --> Sistemde kayıtlı Kullanıcı Adı!")

def giris_yap():
    global name , psw
    name = input("Lütfen hesap Adınızı giriniz: ")  
    psw = input("Lütfen 4 haneli hesap şifrenizi giriniz: ")


def para_ekle():
    global anlik_para, bakiye
    eklenecek_miktar = int(input("Hesabınıza eklemek istediğiniz miktarı giriniz : "))
    print("Eklediğiniz tutar başarıyla hesabınıza yatırıldı.")
    anlik_para = anlik_para + eklenecek_miktar
    bakiye1 = {"hesapName" : anlik_para}
    return bakiye.update(bakiye1)


def para_cek():
    global anlik_para, bakiye
    cekilecek_miktar = int(input("Çekmek istediğiniz tutarı giriniz : "))
    if cekilecek_miktar > anlik_para:
        return False
    anlik_para = anlik_para - cekilecek_miktar
    bakiye2 = {"hesapName" : anlik_para}
    return bakiye.update(bakiye2)
        

def bakiye_sorgula():
    bky = bakiye["hesapName"]
    print(f"Hesap bakiyeniz : {bky}")


def main_menu():
    global anlik_para
    print("¯\_(ツ)_/¯ YAPMAK İSTEDİĞİNİZ İŞLEM NUMARASINI SEÇİN ¯\_(ツ)_/¯")
    print("-"*75)
    global islem
    islem = int(input("[1]Para Yatır\n[2]Para Çek\n[3]Bakiye Sorgula\n[4]Başka hesaba giriş yap\n[5]Kayıt Yap\n=> "))
    
    if islem == 1:
        para_ekle()
    elif islem == 2:
        para_cek()
    elif islem == 3:
        bakiye_sorgula()
    elif islem == 4:
        giris_yap()
        giris_kontrol()
        anlik_para = 0
        return anlik_para
    elif islem == 5:
        kayit_yap()
    else:
        return False


print("-"*75)
def tekrar_islem():
    while True:
        global option
        option = input("Başka işlem Yapmak ister misiniz ? e/h : ")
        if option == "e" or option == "E":
            main_menu()    
        elif option == "h" or option == "H":
            break


def giris_kontrol():
    with open("C:/Users/kadir/Desktop/kullaniciler.txt","r",encoding="utf-8") as file1:
        if name in file1.read():
            main_menu()
            tekrar_islem()
        else:
            print("Sistemde kayıtlı değilsiniz lütfen kayıt olun!")


giris_yap()
giris_kontrol()



