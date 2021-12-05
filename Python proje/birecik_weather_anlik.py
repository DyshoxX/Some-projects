from typing import Text
import requests
from bs4 import BeautifulSoup


url = "https://www.havadurumu15gunluk.xyz/havadurumu/1248/sanliurfa-birecik-hava-durumu-15-gunluk.html"

html = requests.get(url).content # => sayfaya istek gönderdi ve olumlu yanıt alıp içeriğini html şeklinde tuttu aldı (.content)
soup = BeautifulSoup(html, "html.parser")
list = soup.prettify()

sehir = soup.find("aside").find("h3").text.strip()
sicaklik = soup.find("aside").find("span",{"class":"temperature type-1"}).text.strip()

print(f" {sehir[0:18]}için sıcaklık değeri : {sicaklik} ")