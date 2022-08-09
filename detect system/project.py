class kullanici:
    def __init__(self) -> None:
        pass

    def register(self): # txt ye kayıt işlemi gerçekleştiren func

        nickname = str(input("Nickname : "))
        password = str(input("Password : "))
        repeat_password = str(input("Repeat password : "))
        
        if password == repeat_password:
            with open("kayit.txt","r+") as file:
                kullanicilar = file.readlines()
                for line in kullanicilar:
                    if nickname in line and password in line:
                        print("Erorr already has been registered please control nickname or password! ")
                    else:
                        user = f"{nickname} - {password} \n"
                        with open("kayit.txt","a") as file:
                            file.write(user)
                            print("succesfully regestered!")
        else:
            print("Wrong password repeat!")


    def login(self): # eğer kayıt varsa giriş işlemini sağlayan func
        global incelenecek_metin,nickname,password
        
        nickname = str(input("Nickname : "))
        password = str(input("Password : "))
        with open("kayit.txt","r+") as file:
                kullanicilar = file.readlines()
                for line in kullanicilar:
                    if nickname in line and password in line:
                        print("You have succesfully logged in")
                        self.search_text()
                        

    def search_text(self): # giriş yapıldıktan sonra girişi  yapılan kullanıcının incelenmesini istenilen metini kontrol eden func

        wrong_words = [] #metinde olmasını istemedeiğiniz kelimeleri liste şeklinde girmelisiniz
        incelenecek_metin = str(input("Kullanıcının incelenecek metnini giriniz: ")) #Bir uygulama içinde kullanılırsa burası veritabanından otomatik çekebilir kullanıcının şikayet edilen metinlerini

        for w_word in wrong_words:
            if w_word in incelenecek_metin:
                print("user banned from the chat!")
                # with open("kayit.txt","r+") as file:          --->>  banlanan kullanıcıyı kayıtlardan silme kısmı tam çalışmıyor bugu sonra çözerim
                #     kullanicilar = file.readlines()
                #     for line in kullanicilar:
                #         if nickname in line and password in line:
                #             banned_user = line
                #             if line != banned_user:
                #                 with open("kayit.txt","w") as f: 
                #                     f.write(line)
                break
        else:
            print("There isn't any problem in this text")

user = kullanici()              
user.login()