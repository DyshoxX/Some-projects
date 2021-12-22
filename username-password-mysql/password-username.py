import mysql.connector
import time
import pyfiglet
import sys

connection = mysql.connector.connect(host="localhost",user="root",password="mysql1234",database="users")
cursor = connection.cursor()

class user():
    def __init__(self):
        self.connection = connection
        self.cursor = cursor

    def kayit(self):
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")

        #kayıt kontrol:
        sql = "select username from users"
        self.cursor.execute(sql)
        users = self.cursor.fetchall()

        for user in users:  
            kullanici_adı = user[0]  
            if username == kullanici_adı:
                print("Alınmış bir kullanıcı adı girdiniz lütfen farklı bir kullanıcı adı giriniz!")
                break
            else:
                sql = "INSERT INTO users(password,username) VALUES (%s,%s)"
                values = (password,username)
                self.cursor.execute(sql,values)

                try:
                    self.connection.commit()
                except mysql.connector.Error as err:
                    print("hata",err)
                finally:
                    print("Veritabanı bağlantısı kapandı")
                    self.connection.close()
                break

    def giris(self):
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")

        #kayıt kontrol:
        sql = "select * from users"
        self.cursor.execute(sql)
        users = self.cursor.fetchall()

        for user in users:
            password_k = user[1]
            username_k = user[2]

            if (username==username_k) and (password==password_k):
                print("Başarıyla giriş yapıldı!")
                break
        else:
            print("Kullanıcı adı veya parola hatalı!")
                
        
    def change_password(self):
            username = input("Kullanıcı adı: ")
            password = input("Yeni şifre: ")
            password_tekrar = input("Yeni şifre tekrar: ")

            sql = "Select username from users"
            self.cursor.execute(sql)
            users = self.cursor.fetchall()
            for user in users:
                uName = user[0]
                if username == uName:
                    if password == password_tekrar:
                        sql = "Update users Set password=%s where username=%s"
                        values = (password,username)
                        self.cursor.execute(sql,values)

                        try:
                            self.connection.commit()
                            print("Şifre Başarıyla güncellendi!")
                        except mysql.connector.Error as err:
                            print("hata",err)
                        finally:
                            print("Veritabanı bağlantısı kapandı")
                            self.connection.close()
                        break

def main():
    kullanici = user()
    dyshoxx = pyfiglet.figlet_format("made by ->DyshoxX<-")
    print(dyshoxx, """
    1 - kayıt ol
    2 - giriş yap
    3 - şifremi unuttum
    4 - çıkış
    """ )
    choice = input("Seçiminiz : ")
    if choice == "1":
        print("lütfen bekleyin...")
        time.sleep(1)
        kullanici.kayit()

    elif choice == "2":
        print("lütfen bekleyin...")
        time.sleep(1)
        kullanici.giris()

    elif choice == "3":
        print("lütfen bekleyin...")
        time.sleep(1)
        kullanici.change_password()

    elif choice == "4":
        print("çıkılıyor...")
        time.sleep(1)
        sys.exit()

main()
while True:
    devam = input("Başka işlem yapmak istiyor musunuz ? (e/h) :")
    if devam == "e":
        main()
    else:
        break



