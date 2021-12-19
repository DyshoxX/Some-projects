import mysql.connector
import sys
import time 
import pyfiglet

class Kutuphane():
    def __init__(self):
        pass


    def kayit_ekle(self,name,surname,kitap):
        if kitap is None:
            kitap = "none"
            return kitap

        connection = mysql.connector.connect(host = "localhost",user = "root",password = "mysql1234",database = "kutuphane")
        cursor = connection.cursor()

        sql = "INSERT INTO ogrenciler(name,surname,kitap) VALUES (%s,%s,%s)"
        values = (name,surname,kitap)

        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt eklendi")
            print(f"son eklenen kaydın id'si {cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            print("işlemleriniz tamamlanıyor...")
            time.sleep(1)
            connection.close()
            print("Database bağlantısı kapatıldı.")


    def kayit_sil(self,id):
        print("Öğrencinin id sini öğrenmek için kayıtları_listele'yin!")
        connection = mysql.connector.connect(host = "localhost",user = "root",password = "mysql1234",database = "kutuphane")
        cursor = connection.cursor()

        sql = "delete from ogrenciler where id=%s"
        values = (id,)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt silindi")
            print(f"son silinen öğrenci id'si {cursor.lastrowid}")
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            print("işlemleriniz tamamlanıyor...")
            time.sleep(1)
            connection.close()
            print("Database bağlantısı kapatıldı.")
        

    def kayıtları_listele(self):
        connection = mysql.connector.connect(host = "localhost",user = "root",password = "mysql1234",database = "kutuphane")
        cursor = connection.cursor()

        sql = "Select * from ogrenciler"
        cursor.execute(sql)

        try:
            students = cursor.fetchall()
            for student in students:
                print(f"id: {student[0]} - name: {student[1]} - surname: {student[2]} - kitap:{student[3]} ")
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            print("işlemleriniz tamamlanıyor...")
            time.sleep(1)
            connection.close()
            print("Database bağlantısı kapatıldı.")


    def kitap_ver(self,id):
        connection = mysql.connector.connect(host = "localhost",user = "root",password = "mysql1234",database = "kutuphane")
        cursor = connection.cursor()

        sql = "Update ogrenciler Set kitap=%s where id=%s"
        verilecek_kitap = input("Verilecek kitap ismi? : ")
        values = (verilecek_kitap,id)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{id} id ye sahip öğrenciye {verilecek_kitap} kitabı verildi.")
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            print("işlemleriniz tamamlanıyor...")
            time.sleep(1)
            connection.close()
            print("Database bağlantısı kapandı.") 

    def kitap_al(self,id):
        connection = mysql.connector.connect(host = "localhost",user = "root",password = "mysql1234",database = "kutuphane")
        cursor = connection.cursor()

        sql = "Update ogrenciler Set kitap='öğrenciye ait kitap kaydı bulunmamaktadır' where id=%s"
        values = (id,)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{id} id ye sahip öğrencinin kitabı teslim alındı.")
        except mysql.connector.Error as err:
            print("hata",err)
        finally:
            print("işlemleriniz tamamlanıyor...")
            time.sleep(1)
            connection.close()
            print("Database bağlantısı kapandı.") 


def main_menu():
    ogrenci = Kutuphane()
    print(pyfiglet.figlet_format("MADE BY DyshoxX"))
    print("""
    1 - kayıt ekle
    2 - kayıt sil
    3 - kayıtları listele
    4 - kitap ver
    5 - kitap al
    6 - exit
    """)
    yanıt = input("Yapmak istediğiniz işlem numarası? :")

    if yanıt == "1":
        name = input("İsim: ")
        surname = input("Soy İsim: ")
        kitap = "None"
        ogrenci.kayit_ekle(name,surname,kitap)

    elif yanıt == "2":
        delete_id = input("Silinecek kaydın (öğrenciye ait) id :")
        ogrenci.kayit_sil(delete_id)

    elif yanıt == "3":
        ogrenci.kayıtları_listele()

    elif yanıt == "4":
        delete_id = input("Silinecek kaydın (öğrenciye ait) id :")
        ogrenci.kitap_ver(delete_id)

    elif yanıt == "5":
        delete_id = input("Silinecek kaydın (öğrenciye ait) id :")
        ogrenci.kitap_al(delete_id)

    elif yanıt == "6":
        print("Programdan çıkılıyor...")
        time.sleep(1)
        sys.exit()


main_menu()
while True:    
    islem = input("Başka işlem yapmak istiyor musunuz? (e/h) :")
    if islem == "e":
        main_menu()

    elif islem == "h":
        break




