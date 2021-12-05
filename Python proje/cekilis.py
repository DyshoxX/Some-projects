import random

print(" "*21)
print("Çekiliş uygulamamıza hoşgeldiniz! ")
print("_-"*21)

oge_adet = int(input("Kura çekilecek öge sayısını giriniz: "))
list = []

def listeyi_al():
    for i in range(0,oge_adet):
        oge = str(input("kura çekilecek kelime: "))
        list.append(oge)

listeyi_al()

print("_-"*21)
print(f"Kazanan: {random.choice(list)}")
input("_-"*21)
