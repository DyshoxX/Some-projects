import random
import time

mid_heros = ["akali","zed","yasuo","yone","talon","galio","pantheon","anivia","katarina","lucian","akshan"]
solo_heros = ["akali","aatrox","kayle","vayne","teemo","sett","yasuo","darius","garen","quinn","yone","malphite"]
adc_heros = ["miss fortune","kai sa","ezreal","yasuo","vayne","ashe","lucian","xayah","kalista","sivir"]
sup_heros = ["yuumi","sett","tahm kench","shen","rakan","pyke","blitzcrank","bard","soraka","lulu","leona","malphite"]
jungle_heros = ["lee sin","kayn","master yi","trundle","rek sai","lillia","volibear","kha zix","hecarim","jax","graves"]

def hero_belirle():
    secim  = int(input("[1]MİD\n[2]SOLO\n[3]ADC\n[4]SUP\n[5]JUNGLE\n=>oynamak istediğiniz rol? : "))
    print("-"*30)
    if secim == 1:
        hero = random.choice(mid_heros)
        time.sleep(1)
        print(f"MİD tier listten rastgele hero : {hero}")

    elif secim == 2:
        hero = random.choice(solo_heros)
        time.sleep(1)
        print(f"SOLO tier listten rastgele hero : {hero}")

    elif secim == 3:
        hero = random.choice(adc_heros)
        time.sleep(1)
        print(f"ADC tier listten rastgele hero : {hero}")

    elif secim == 4:
        hero = random.choice(sup_heros)
        time.sleep(1)
        print(f"SUP tier listten rastgele hero : {hero}")

    elif secim == 5:
        hero = random.choice(jungle_heros)
        time.sleep(1)
        print(f"JUNG tier listten rastgele hero : {hero}")

    else:
        print("girdiğiniz sayıyı kontrol edip tekrar deneyiniz :/ ")
 

def rol_belirle():
    roles = [1,2,3,4,5]
    role = random.choice(roles)
    if role == 1:
        hero = random.choice(mid_heros)
        time.sleep(1)
        print(f"MİD tier listten rastgele hero : {hero}")
    elif role == 2:
        hero = random.choice(solo_heros)
        time.sleep(1)
        print(f"SOLO tier listten rastgele hero : {hero}") 
    elif role == 3:
        hero = random.choice(adc_heros)
        time.sleep(1)
        print(f"ADC tier listten rastgele hero : {hero}")
    elif role == 4:
        hero = random.choice(sup_heros)
        time.sleep(1)
        print(f"SUP tier listten rastgele hero : {hero}")
    elif role == 5:
        hero = random.choice(jungle_heros)
        time.sleep(1)
        print(f"JUNG tier listten rastgele hero : {hero}")

def choice_belirle():
    choice = int(input("[1]Rolü kendim belirlemek istiyorum.\n[2]Rastgele rol\n=> "))
    if choice == 1:
        print("-"*30)
        hero_belirle()
        print("-"*30)

    elif choice == 2:
        print("-"*30)
        rol_belirle()
        print("-"*30)
choice_belirle()

while True:
    islem = str(input("Başka işlem yapmak istiyor musunuz? e/h : "))
    if islem == "e":
        choice_belirle()
    elif islem == "h":
        break