import mysql.connector
from PyQt5 import QtWidgets
from anasayfa import MainWindow
from kitapver import KitapVer
from ogr_ekle import OgrenciEkle
import sys

class kutuphane_otomasyon(QtWidgets.QMainWindow):
    def __init__(self):
        super(kutuphane_otomasyon,self).__init__()     
        #ANASAYFA KURULUM:
        self.anasayfa = MainWindow()
        self.anasayfa.setupUi(self)

        #CLİCK EVENT OLAYLARI:
        self.anasayfa.ogr_ekle_button.clicked.connect(self.anasayfa_ogrenci_ekle)
        self.anasayfa.kitap_ver_input.clicked.connect(self.anasayfa_kitap_ver)

    def anasayfa_ogrenci_ekle(self):
        #ANASAYFA KURULUM:
        self.pencere = QtWidgets.QMainWindow()
        self.ogrenciekle = OgrenciEkle()
        self.ogrenciekle.setupUi(self.pencere)
        
        self.pencere.show()

        #CLİCK EVENT OLAYLARI:
        self.ogrenciekle.ogr_save_button.clicked.connect(self.ogrenci_ekle)
    
    def ogrenci_ekle(self):
        name = self.ogrenciekle.ogr_ad_input.text()
        surname = self.ogrenciekle.ogr_soyad_input.text()
        no = self.ogrenciekle.ogr_no_input.text()
        kitap = "null"

        connection = mysql.connector.connect(host="yourhost",user="youruser",password="yourpassword",database="yourdatabase",port='3306')
        cursor = connection.cursor()

        sql = "INSERT INTO deneme(name,surname,no,kitap) VALUES (%s,%s,%s,%s)"
        values = (name,surname,no,kitap)
        cursor.execute(sql,values)

        try:
            connection.commit()
            self.ogrenciekle.ogr_save_button.setText("Eklendi!")
        except mysql.connector.Error as err:
            print("Hata!",err)
        finally:
            print("Database Bağlantısı kapandı!")
            connection.close()

    def anasayfa_kitap_ver(self):
        #ANASAYFA KURULUM:
        self.pencere = QtWidgets.QMainWindow()
        self.kitapver = KitapVer()
        self.kitapver.setupUi(self.pencere)
        
        self.pencere.show()

        #CLİCK EVENT OLAYLARI:
        self.kitapver.kitab_ver_input.clicked.connect(self.kitap_ver)

    def kitap_ver(self):
        name = self.kitapver.ad_input.text()
        no = self.kitapver.ogr_no_input.text()
        kitap = self.kitapver.kitap_adi_input.text()

        connection = mysql.connector.connect(host="yourhost",user="youruser",password="yourpassword",database="yourdatabase",port='3306')
        cursor = connection.cursor()

        sql = "UPDATE deneme set kitap=%s Where no=%s"
        values = (kitap,no)
        cursor.execute(sql,values)

        try:
            connection.commit()
            self.kitapver.kitab_ver_input.setText("Kitap verildi!")
        except mysql.connector.Error as err:
            print("Hata!",err)
        finally:
            print("Database Bağlantısı kapandı!")
            connection.close()


def main():
    main = QtWidgets.QApplication(sys.argv)
    win = kutuphane_otomasyon()
    win.show()
    sys.exit(main.exec_())

main()
