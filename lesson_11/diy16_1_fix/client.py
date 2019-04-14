# -*- coding: utf-8 -*-

"""
   程式說明請參閱16-15頁
"""
import sys
import socket
s = socket.socket()
if len(sys.argv) > 1:
    s.connect((sys.argv[1], 5438))
else:
    s.connect(('127.0.0.1', 5438))
while True:
    msg = input('請輸入訊息：').strip()
    s.send(msg.encode('utf8'))
    reply = s.recv(128)
    if reply == b'quit':
        print('關閉連線')
        s.close()
        break
    print(str(reply))
