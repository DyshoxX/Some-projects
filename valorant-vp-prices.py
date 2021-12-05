from bs4 import BeautifulSoup
import requests

url = "https://www.trendyol.com/sr?q=Valorant%20vp&qt=Valorant%20vp&st=Valorant%20vp&os=1"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

vp = soup.find("div",{"id":"container"}).find_all("div",{"class":"prc-box-sllng"})
liste = []
for i in vp:
    liste.append(i.text)

print("*"*50)
print(f"> 300 VP --> {liste[2]}\n> 600 VP --> {liste[3]}\n> 1250 VP --> {liste[1]}\n> 2500 VP --> {liste[0]}\n> 4400 VP --> {liste[4]}\n> 8800 VP --> {liste[5]}")
print("*"*50)
print("Daha fazlası için :\nhttps://www.google.com/search?q=valorant+vp&oq=valorant+vp&aqs=chrome.0.0i433i512j0i512j0i433i512j0i512l7.1391j0j7&sourceid=chrome&ie=UTF-8")
print("*"*50)
input("Çıkmak için bir tuşa basınız...")