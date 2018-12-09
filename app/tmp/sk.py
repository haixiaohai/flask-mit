from socket import *

sk = socket()


sk.bind(('192.168.111.3',10000))
sk.listen(5)

print('starting')
conn,addr=sk.accept()
print(conn,addr)

client_msg=conn.recv(1024)
print('client msg:%s' %client_msg)

conn.send(client_msg.upper())
conn.close()
sk.close()