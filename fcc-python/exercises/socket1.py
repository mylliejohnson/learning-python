import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org", 80)) 
# domain name, tuple, port 80
cmd = "GET http://data.pr4e.org/romeo.txt HTTP:/1.0\n\n".encode() 
# encode converts string unicode to utf8 
mysock.send(cmd) 
# mysock is file handle

while True:
    data = mysock.recv(512) 
    # 512 characters
    if (len(data) < 1): 
        # end of file if data length < 1
        break
    print(data.decode())
    # utf8 to unicode
mysock.close()