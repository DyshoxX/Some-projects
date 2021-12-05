hesapName = "hesapname"
hesapSifre = "1234"

anlik_para = 0
bakiye = {hesapName : anlik_para}

def giris_yap():
    global name , psw
    name = input("Lütfen hesap Adınızı giriniz: ")  
    psw = input("Lütfen 4 haneli hesap şifrenizi giriniz: ")


def para_ekle():
    global anlik_para, bakiye
    eklenecek_miktar = int(input("Hesabınıza eklemek istediğiniz miktarı giriniz : "))
    print("Eklediğiniz tutar başarıyla hesabınıza yatırıldı.")
    anlik_para = anlik_para + eklenecek_miktar
    bakiye1 = {hesapName : anlik_para}
    return bakiye.update(bakiye1)


def para_cek():
    global anlik_para, bakiye
    cekilecek_miktar = int(input("Çekmek istediğiniz tutarı giriniz : "))
    if cekilecek_miktar > anlik_para:
        return False
    anlik_para = anlik_para - cekilecek_miktar
    bakiye2 = {hesapName : anlik_para}
    return bakiye.update(bakiye2)
        

def bakiye_sorgula():
    bky = bakiye[hesapName]
    print(f"Hesap bakiyeniz : {bky}")


def main_menu():
    print("¯\_(ツ)_/¯ YAPMAK İSTEDİĞİNİZ İŞLEM NUMARASINI SEÇİN ¯\_(ツ)_/¯")
    print("-"*75)
    global islem
    islem = int(input("[1]Para Yatır\n[2]Para Çek\n[3]Bakiye Sorgula\n[4]Başka hesaba giriş yap\n=> "))
    
    if islem == 1:
        para_ekle()
    elif islem == 2:
        para_cek()
    elif islem == 3:
        bakiye_sorgula()
    elif islem == 4:
        giris_yap()
        giris_kontrol()
        
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
    if (name == hesapName) and (psw == hesapSifre):
        main_menu()
        tekrar_islem()
    else:
        return False


giris_yap()
giris_kontrol()

