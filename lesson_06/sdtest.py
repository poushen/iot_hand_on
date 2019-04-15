#
# sdtest.py
#
from machine import Pin, SPI
import os, sdcard, gc

try:
     sd = sdcard.SDCard(SPI(1), Pin(15))
except:
    #do again
    sd = sdcard.SDCard(SPI(1), Pin(15))

vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')

os.listdir('/')
s = os.statvfs('/sd')
print()
print('SD Card Info:')
print('Block Size: {}, Capacity: {}MB'.format(s[0], s[0]*s[2]/1024/1024))
print('Remaining Capacity: {}MB'.format(s[0]*s[4]/1024/1024))

print()
print('Remove file')
os.remove('/sd/test.txt')

print()
print('write file')
with open('/sd/test.txt', 'a') as f:
    f.write('hello\r\nworld\r\n')
    
print()
print('read file')
print('-------------------')
with open('/sd/test.txt') as f:
    while True:
        str = f.readline()
        if str != '':
            print(str, end='')
        else:
            break
print('-------------------')

print()
print('umount')
os.umount('/sd')
gc.collect()
# os.listdir()