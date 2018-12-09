from socket import *

sk1 = socket()
sk1.connect(('192.168.1.5',10000))

sk1.send('Hello'.encode('utf-8'))
back_msg=sk1.recv(1024)
print(back_msg)
sk1.close()