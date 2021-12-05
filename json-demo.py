import json
class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email= email

        
class UserReporitory:
    def __init__(self):
        self.users = [] 
        self.isLoogedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUser()

    def loadUser(self):
        pass
    
    def register(self, user: User):
        self.users.append(user)
        # self.saveToFile()
        print("kullanıcı oluşturuldu.")

    def login(self):
        pass
   
    def saveToFile(self):
        with open("users.json","w",encoding="utf-8") as file:
            json.dump(self.users, file)


reporitory = UserReporitory()

while True:
    print("Menü".center(50,"*"))
    secim = input("1- Registern\n2- Login\n3- Logout\n4- identity\n5- Exit\n Seçiminiz: ")
    if secim == "5":
        break
    else:
        if secim == "1":
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username=username, password=password ,email=email)
            reporitory.register(user)


        elif secim == "2":
            # Login
            pass
        elif secim == "3":
            # Logout
            pass
        elif secim == "4":
            #identity
            pass
        else: 
            print("Yanlış Seçim!")