import time
import am2320
import ssd1306
from machine import I2C, Pin
#i2c = I2C(scl=Pin(5), sda=Pin(4))
i2c = I2C(1)
sensor = am2320.AM2320(i2c)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    sensor.measure()
    #print('Temp: {}{}C, Humi: {} %'.format(sensor.temperature(), '\u00b0', sensor.humidity()))
    #print('Temp: {}C, Humi: {} %'.format(sensor.temperature(), sensor.humidity()))
    oled.fill(0)
    oled.text('{:0.1f}C'.format(sensor.temperature()), 20, 20)
    oled.text('{:0.1f}%'.format(sensor.humidity()), 20, 40)
    oled.show()
    time.sleep(4)
