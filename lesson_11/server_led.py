# -*- coding: utf-8 -*-

"""
   程式說明請參閱16-19頁
"""

from machine import Pin
led = Pin(2, Pin.OUT, value=1)

import socket, sys, gc
HOST = '0.0.0.0'
PORT = 5438
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # reuse address
s.bind((HOST, PORT))
s.listen(5)
print('{}伺服器在{}埠開通了！'.format(HOST, PORT))

try:
    client, addr = s.accept()
except:
    print('bye bye')
    s.close()
    gc.collect()
    sys.exit()

print('用戶端位址：{}，埠號：{}'.format(addr[0], addr[1]))

while True:
    msg = client.recv(100).decode('utf8').strip()
    print ('收到訊息：' + msg)
    reply = ''

    if msg == '你好':
        reply = b'Hello!'
    elif msg == '再見':
        break
    elif msg == 'bye':
        break
    elif msg == 'on':
        led.value(0)
        reply = b'ok led on'
    elif msg == 'off':
        led.value(1)
        reply = b'ok led off'
    else:
        reply = b'what??'

    client.send(reply)

client.send(b'quit')
client.close()
s.close()
gc.collect()
print('mem free: {}'.format(gc.mem_free()))
