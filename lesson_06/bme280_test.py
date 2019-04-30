'''
Driver from : https://github.com/catdog2/mpy_bme280_esp8266
Notes: download bme280.py first, then upload to D1 Mini board
'''

from machine import I2C, Pin
import bme280

i2c = I2C(scl=Pin(5), sda=Pin(4))
bme = bme280.BME280(i2c=i2c)

print(bme.values)
print(bme.read_compensated_data())
print('Temperature: {:.2f}{}C'.format(bme.read_compensated_data()[0] / 100, '\u00b0'))
print('Humidity: {:.2f}%'.format(bme.read_compensated_data()[2] / 1024))