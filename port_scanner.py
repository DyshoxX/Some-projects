import socket 
import pyfiglet

ascii_banner =  pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

site = input("Hedef site: ")
target = socket.gethostbyname(site)

print("-" * 50)
print("Hedef taranıyor: " + target)
print("-" * 50)

try:
    for port in range(1 , 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0 :
            print(f"Port {port} açık")
        s.close()

except Exception as e:
    print("Hata !", e)
