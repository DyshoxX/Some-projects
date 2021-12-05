a = int(input("İlk sayıyı giriniz: "))
b = int(input("İkinci sayıyı giriniz: "))


def girilenSayilarArasıAsal(sayi1,sayi2):
    lists = []
    for i in range(sayi1,sayi2+1):
        if i > 1:
            for x in (2,i):
                if (i % x) == 0:
                    break
                else:
                    lists.append(i)
    
    print(f"Girdiğiniz {sayi1}' sayısı ile {sayi2}' sayısı arasındaki asal sayılar: ",lists) 

girilenSayilarArasıAsal(a,b)

input("Çıkmak için Enter'e basınız. ")