import sys
import pyfiglet

class decoder():
    def __init__(self):
        self.params = [(" ","0"),("a","x"),("b","y"),("c","E"),("ç","r"),("d","2"),("e","1"),("f","5"),("g","q"),("ğ","T"),("h","t"),("ı","e"),("i","i"),("j","f"),("k","a"),("l","n"),("m","7"),("n","4"),("o","?"),("ö","*"),("p","6"),("r","h"),("s","Y"),("ş","v"),("t","c"),("u","Z"),("ü","/"),("v","3"),("y","u"),("z","Q"),("0","#"),("1","%"),("2","U"),("3","^"),("4","N"),("5","m"),("6","k"),("7","K"),("8","-"),("9","&")]

    def crypt_password(self):
        password = input("Şifreniz:")
        password = password.lower()

        list = []
        i = 0
        for letter in password:
            for param in self.params:
                parametre = param[0]
                if letter == parametre:
                    parametre = param[1]
                    list.append(parametre)
                i += 1

        crypted_password = ""
        for harf in list:
            crypted_password = crypted_password + harf
                    

        print(f"crypt edilmiş şifreniz : {crypted_password}")
                

    def encrypt_password(self,encript_edilecek):
        sifre = encript_edilecek
        list = []
        i = 0
        for letter in sifre:
            for param in self.params:
                parametre = param[1]
                if letter == parametre:
                    parametre = param[0]
                    list.append(parametre)
                i += 1
    
        encrypted_password = ""
        for harf in list:
            encrypted_password = encrypted_password + harf
                             
        print(f"encrypt edilmiş şifreniz : {encrypted_password}")

ornek = decoder() 
def main():
    print(pyfiglet.figlet_format("made by DyshoxX"))  
    secim = input("""
     ŞİFRELEME-ÇÖZÜMLEME PROGRAMINA HOŞGELDİNİZ !
     1 - Şifrele
     2 - Çözümle
     3 - Çıkış 
     """)
    if secim == "1":
        ornek.crypt_password()
    elif secim == "2":
        encript_edilecek = input("Çözümlenek istediğiniz metni girin: ")
        ornek.encrypt_password(encript_edilecek)
    elif secim == "3":
        sys.exit()
main()

okContinue = input("Devam etmek istiyor musunuz ? (e/h) :")
while True:
    if okContinue == "e":
        main()
    else:
        break


ornek.encrypt_password()

#BÜYÜK KÜÇÜK HARF DUYARLILIĞI YOKTUR EKLENEBİLİR.