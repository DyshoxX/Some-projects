import mysql.connector
import sys
import time
import pyfiglet

class arac():
    def __init__(self):
        pass

    def arac_ekle(self,model,plaka,kullanıcı):
        connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="arac")
        cursor = connection.cursor()

        sql = "INSERT INTO araclar(model,plaka,kullanıcı) VALUES (%s,%s,%s)"
        values = (model,plaka,kullanıcı)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} tane kayıt eklendi.")
        except mysql.connector.Error as err:
            print("Hata!",err)
        finally:
            connection.close()
            print("Database bağlantısı kapandı.")

    def arac_al(self,id):
        connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="arac")
        cursor = connection.cursor()

        sql = "Update araclar set kullanıcı='none' Where id =%s"
        values = (id,)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{id} ye sahip kullanıcı üzerindeki araç alındı.")
        except mysql.connector.Error as err:
            print("Hata!",err)
        finally:
            connection.close()
            print("Database bağlantısı kapandı.")
    
    def arac_ver(self,id,kullanıcı):
        connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="arac")
        cursor = connection.cursor()

        sql = "Update araclar set kullanıcı=%s Where id =%s"
        values = (kullanıcı,id)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{id} ye sahip araç, {kullanıcı} adlı kullanıcıya verildi.")
        except mysql.connector.Error as err:
            print("Hata!",err)
        finally:
            connection.close()
            print("Database bağlantısı kapandı.")
        

    def aracları_listele(self):
        connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="arac")
        cursor = connection.cursor()

        sql = "Select * from araclar"
        cursor.execute(sql)

        araclar = cursor.fetchall()
        for arac in araclar:
            print(f"Id : {arac[0]} , Model : {arac[1]} , Plaka : {arac[2]} , Kullanıcı: {arac[3]}")

def main_menu():
    araba = arac()
    print(pyfiglet.figlet_format("MADE BY DyshoxX"))
    print("""
    1 - araç ekle
    2 - araç ver
    3 - araç teslim al
    4 - araçları listele
    5 - exit 
    """)
    choice = input("Seçiminiz? = ") 
    if choice == "1":
        model = input("Araç modeli : ")
        plaka = input("eklemek istediğiniz aracın plakası : ")
        kullanıcı = "none"
        print("Yükleniyor...")
        time.sleep(1)
        araba.arac_ekle(model,plaka,kullanıcı)

    elif choice == "2":
        id = input("Vermek istediğiniz araç id'si : ")
        kullanıcı = input("Aracı vermek istediğiniz şahıs isim-soy isim ? : ")
        print("Yükleniyor...")
        time.sleep(1)
        araba.arac_ver(id,kullanıcı)

    elif choice == "3":
        id = input("Teslim almak istediğiniz araç id'si : ")
        print("Yükleniyor")
        time.sleep(1)
        araba.arac_al(id)

    elif choice == "4":
        print("Yükleniyor...")
        time.sleep(1)
        araba.aracları_listele()

    elif choice == "5":
        print("Çıkılıyor...")
        time.sleep(1)
        sys.exit()

main_menu()
while True:
    secim = input("Başka işlem yapmak istiyor musunuz ? (e/h) : ")
    if secim == "e":
        print("Yükleniyor...")
        time.sleep(1)
        main_menu()
    elif secim == "h":
        print("programdan çıkılıyor...")
        time.sleep(1)
        break
    else:
        print("Girdğiniz değeri kontrol ediniz!!!")

