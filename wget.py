#coding : utf-8
import socket
import sys
import urlparse
import select
url = urlparse.urlparse(sys.argv[1])
port = 80
gniazdo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gniazdo.connect((url.hostname, port))
gniazdo.sendall("GET "+url.path+"  HTTP/1.1\r\nHost: "+url.hostname+"\r\n\r\n")
tmp = url.path.split('/')[-1]
reply = b''
data = gniazdo.recv(10000)
reply += data
headers =  reply.split(b'\r\n\r\n')[0]
wynik = reply[len(headers)+4:]
plik = open(tmp, 'wb')
plik.write(wynik)
plik.close()