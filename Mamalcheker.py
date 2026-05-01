import socket

#شروع

TARGET = input("Enter host : ")
print(socket.gethostbyname(TARGET))
COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 8080, 3389, 5900]

def check_port(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((TARGET, port))
        return True
    except:
        return False
    finally:
        s.close()

print(f"اسکن پورت‌ها روی {TARGET} …")
for p in COMMON_PORTS:
    if check_port(p):
        print(f"[+] پورت {p} باز است")
    else:
        print(f"[-] پورت {p} بسته است")
