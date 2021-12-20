import bigSymbol
from machine import Pin, I2C
from time import sleep
import ssd1306, am2320
i2c = I2C(1)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
sensor = am2320.AM2320(i2c)

dsp = bigSymbol.Symbol(oled)
dsp.clear()
dsp.temp(0, 18)
dsp.humid(0, 38)
while True:
    sensor.measure()
    # dsp.text('18.50c', 34, 18)
    # dsp.text('25.00%', 34, 38)
    dsp.text('{:.2f}c'.format(sensor.temperature()), 34, 18)
    dsp.text('{:.2f}%'.format(sensor.humidity()), 34, 38)   
    oled.show()
    sleep(4)