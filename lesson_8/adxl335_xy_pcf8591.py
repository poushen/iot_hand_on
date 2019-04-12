from machine import Pin, I2C
import time

PCF8591 = 0x48
CH0 = b'\x00'
CH1 = b'\x01'

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

while True:
    r = i2c.writeto(PCF8591, CH0)
    data0 = i2c.readfrom(PCF8591, 1)
    data0 = i2c.readfrom(PCF8591, 1)
    
    r = i2c.writeto(PCF8591, CH1)
    data1 = i2c.readfrom(PCF8591, 1)
    data1 = i2c.readfrom(PCF8591, 1)
    
    # calculate g value
    x = (data0[0] - 128) / 256 * 3.3 / 0.3
    y = (data1[0] - 128) / 256 * 3.3 / 0.3
    
    print('x = {:.2f}g \t\t y = {:.2f}g'.format(x, y))
    
    time.sleep_ms(100)