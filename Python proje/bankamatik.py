# Bankamatik uygulaması: 

SadikHesap = {
    "ad": "Sadık Turan",
    "hesapNo" : "123456789",
    "bakiye" : 3000,  
    "ekHesap" : 2000
}

AliHesap = {
    "ad": "Ali Turan",
    "hesapNo" : "123456789",
    "bakiye" : 2000,  
    "ekHesap" : 1000
}

def paraCek(hesap, miktar):

    print(f"Merhaba {hesap['ad']} ")

    if (hesap["bakiye"] >= miktar):
        hesap["bakiye"] -= miktar
        print("paranızı alabilirsiniz")
        bakiyeSorgula(SadikHesap)

    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        
        if (toplam >= miktar):
            ekHesapKulanimi = input("Ek hesap kullanılsın mu = (e/h) ")

            if ekHesapKulanimi == "e":
                ekHesapKulanilacakMiktar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekHesapKulanilacakMiktar
                print("paranızı alabilirsiniz")
                bakiyeSorgula(SadikHesap)
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bakiye bulunmaktadır. ")

        else: 
            print("üzgünüz bakiye yetersiz. ")
            bakiyeSorgula(SadikHesap)


def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu heabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL . ")


def paraEkle(hesap, miktar):
    print(f"Merhaba {hesap['ad']} ")

    eklenecek = int(input("Eklemek istediğiniz miktarı giriniz: "))
    # print(f"yeni bakiyeniz = {hesap['bakiye'] + eklenecek }")
    hesap['bakiye'] = hesap['bakiye'] + eklenecek
    bakiyeSorgula(SadikHesap)
    return hesap['bakiye'] 
    
def paraEkleEkHesap(hesap, miktar):
    print(f"Hoşgeldiniz {hesap['ad']}")

    ekHesapEkle = int(input("Ek hesabınıza eklemek istediğiniz miktarı giriniz: "))
    hesap["ekHesap"] = hesap["ekHesap"] + ekHesapEkle
    bakiyeSorgula(SadikHesap)
    return hesap["ekHesap"]     



paraCek(SadikHesap, 1000)

print("*************************")

paraCek(SadikHesap, 500)

print("*"*20)

paraEkle(SadikHesap,1000)

print("*"*20)

paraEkleEkHesap(SadikHesap, 1000)

input("Çıkmak için Enter' a basınız. ")