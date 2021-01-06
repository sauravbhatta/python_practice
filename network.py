#HTTP is a set of rules that allow browsers to retrieve web documents from servers over the internet .
#http://www.ksb.com/page.htm 

"""
import socket
my_sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org',80))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

while True:
      data=my_sock.recv(512)
      if(len(data)<1):
         break
      print(data.decode())
my_sock.close()

Output
MNGNET1477D:python_special saurav.b01$ python network.py
HTTP/1.1 200 OK
Date: Tue, 01 Dec 2020 13:32:12 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "a7-54f6609245537"
Accept-Ranges: bytes
Content-Length: 167
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain

But soft what light through yonder window breaks
It is the east and Juliet is the sun
Arise fair sun and kill the envious moon
Who is already s
ick and pale with grief

#The urllib.request modules have been deprecated .. just use

import urllib

fhand= urllib.urlopen('http://data.pr4e.org/romeo.txt')
for l in fhand:
    print(l.decode().strip())
"""

import urllib

fhand= urllib.urlopen('http:www.google.com')
for l in fhand:
    print(l.decode().strip())