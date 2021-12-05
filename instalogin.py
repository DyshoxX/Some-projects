from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

username = "cristiano"
password = "yourpassword"

ayarlar = Options()
ayarlar.add_argument("--headless")

def login():
    url = "https://www.instagram.com/accounts/login/"

    browser = webdriver.Chrome("C:/Users/kadir/Desktop/Yeni klasör/chromedriver.exe")
    browser.get(url)
    time.sleep(1)

    username_yolu = browser.find_element_by_name("username")
    password_yolu = browser.find_element_by_name("password")

    username_yolu.send_keys(username)
    password_yolu.send_keys(password)

    loginbutton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
    loginbutton.click()

    time.sleep(3)

    simdi_degil = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    simdi_degil.click()

    arama = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    arama.send_keys(username)
    arama.click()
    arama.send_keys(Keys.ENTER)
    arama.send_keys(Keys.ENTER)

    time.sleep(5)
    browser.close()

def takipci_sayisi():
    url = "https://www.instagram.com/" + username
    
    browser = webdriver.Chrome("C:/Users/kadir/Desktop/Yeni klasör/chromedriver.exe")
    browser.get(url)
    time.sleep()

    takipciSayisi = browser.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/ul/li[2]/a/span').text
    print(f"{username} adlı hesabın anlık {takipciSayisi} takipçisi var!")

takipci_sayisi()


