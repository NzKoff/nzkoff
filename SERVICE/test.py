
import socket

import re
FLAG_FORMAT = r"[a-zA-Z0-9\-\%#$]{35}\+"

def find_flags(data):
    return re.findall(FLAG_FORMAT, data) or []

def check(flag):
    HOST = '192.168.43.234'  # Адрес чекера
    PORT = 31337  # Порт чекера
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    answer = None
    print('flag = ', flag)
    try:
        s.connect((HOST, PORT))
        msg = s.recv(1024)
        print(msg)
        print(flag.encode() + "\n".encode())
        s.sendall(flag.encode() + "\n".encode())
        answer = s.recv(1024)
        print('and = ', answer)
    except socket.error as msg:
        pass
    finally:
        s.close()
        return answer


print(check("mR$gGQztdeAX3d7Gd$m-s%1SttC0lT#xf%w+"))