from os import device_encoding
import mysql.connector
import pyfiglet
import time
import sys

connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="banka")
cursor = connection.cursor()

class ATM():
    def __init__(self):
        self.connection = connection
        self.cursor = cursor


    def kayit_ol(self):
        ad = input("Adınız : ")
        soyad = input("Soyadınız : ")
        kartno = input("kart numaranız : ")
        sifre = input("kart şifreniz : ")
        bakiye = "0"

        sql = "INSERT INTO atm(ad,soyad,kartno,sifre,bakiye) VALUES (%s,%s,%s,%s,%s)"
        values = (ad,soyad,kartno,sifre,bakiye)
        self.cursor.execute(sql,values)

        try:
            self.connection.commit()
            print(f"{ad} {soyad} ---> {kartno} kart numarasıyla sisteme başarıyla kaydedildi ")
        except mysql.connector.Error as err:
            print("Hata!",err)
        finally:
            print("Veritabanı bağlantısı kesildi")
            self.connection.close()


    def giris_yap(self):
        kartno = input("kart numaranız : ")
        sifre = input("Kart şifreniz : ")
    
        # kart no alcaz
        sql = "Select kartno from atm"
        self.cursor.execute(sql)
        kartNoları = self.cursor.fetchall()

        for kartNo in kartNoları:
            kartNo = kartNo[0]
            if kartno == kartNo:
                sql = "Select sifre from atm"
                self.cursor.execute(sql)
                sifreler = self.cursor.fetchall()
                for psw in sifreler:
                    psw = psw[0]
                    if psw == sifre:
                        print("Başarıyla giriş yapıldı!")
                        break
                else:
                    print("Lütfen girdiğiniz kart numarası veya 4 haneli kart şifrenizi kontrol ediniz!")


    def para_yatir(self):
        kartno = input("kart numaranız : ")
        sifre = input("Kart şifreniz : ")
    
        sql = "Select kartno from atm"
        self.cursor.execute(sql)
        kartNoları = self.cursor.fetchall()

        for kartNo in kartNoları:
            kartNo = kartNo[0]
            if kartno == kartNo:
                sql = "Select sifre from atm"
                self.cursor.execute(sql)
                sifreler = self.cursor.fetchall()
                for psw in sifreler:
                    psw = psw[0]
                    if psw == sifre:
                        sql = "Select bakiye from atm where kartno=%s"
                        values = (kartno,)
                        self.cursor.execute(sql,values)
                        old_bakiye = self.cursor.fetchall()
                        for bakiye in old_bakiye:
                            bakiye = bakiye[0]
                            eklenecek = input("Lütfen bakiyenize eklemek istediğiniz tutarı giriniz : ")
                            new_bakiye = int(bakiye) + int(eklenecek)
                            sql = "Update atm Set bakiye=%s where kartno=%s"
                            values = (new_bakiye,kartno)
                            self.cursor.execute(sql,values)
                            try:
                                self.connection.commit()
                            except mysql.connector.Error as err:
                                print("Hata!",err)
                            finally:
                                print(f"Yeni bakiyeniz --> {new_bakiye}")

            else:
                print("Lütfen girdiğiniz kart numarası veya 4 haneli kart şifrenizi kontrol ediniz!")
        
    
    def para_cek(self):
        kartno = input("kart numaranız : ")
        sifre = input("Kart şifreniz : ")
    
        sql = "Select kartno from atm"
        self.cursor.execute(sql)
        kartNoları = self.cursor.fetchall()

        for kartNo in kartNoları:
            kartNo = kartNo[0]
            if kartno == kartNo:
                sql = "Select sifre from atm"
                self.cursor.execute(sql)
                sifreler = self.cursor.fetchall()
                for psw in sifreler:
                    psw = psw[0]
                    if psw == sifre:
                        sql = "Select bakiye from atm where kartno=%s"
                        values = (kartno,)
                        self.cursor.execute(sql,values)
                        old_bakiye = self.cursor.fetchall()
                        for bakiye in old_bakiye:
                            bakiye = bakiye[0]
                            cekilecek = input("Lütfen bakiyenizden çekmek istediğiniz tutarı giriniz : ")
                            new_bakiye = int(bakiye) - int(cekilecek)
                            if new_bakiye >= 0:
                                sql = "Update atm Set bakiye=%s where kartno=%s"
                                values = (new_bakiye,kartno)
                                self.cursor.execute(sql,values)
                                try:
                                    self.connection.commit()
                                except mysql.connector.Error as err:
                                    print("Hata!",err)
                                finally:
                                    print(f"Yeni bakiyeniz --> {new_bakiye}")
                                    self.connection.close()
                            else:
                                print(f"Çekebileceğiniz maximum tutar : {bakiye} tl'dir!")

            else:
                print("Lütfen girdiğiniz kart numarası veya 4 haneli kart şifrenizi kontrol ediniz!")


musteri = ATM()
def main():
    print(pyfiglet.figlet_format("_made by_ ->DyshoxX<-"))
    choice = input("""
    1 - hesap ekle
    2 - giriş yap
    3 - para yatır
    4 - para çek
    5 - çıkış yap
    ===>  """)
    if choice == "1":
        print("yükleniyor...")
        time.sleep(1)
        musteri.kayit_ol()

    elif choice == "2":
        print("yükleniyor...")
        time.sleep(1)
        musteri.giris_yap()

    elif choice == "3":
        print("yükleniyor...")
        time.sleep(1)
        musteri.para_yatir() 

    elif choice == "4":
        print("yükleniyor...")
        time.sleep(1)
        musteri.para_cek()

    elif choice == "5":
        print("Çıkılıyor...")
        time.sleep(1)
        sys.exit() 

main()
while True:
    print(pyfiglet.figlet_format("----------"))
    devam = input("Başka işlem yapmak istiyor musunuz ? (e/h) :")
    if devam == "e":
        main()
    elif devam == "h":
        break 
