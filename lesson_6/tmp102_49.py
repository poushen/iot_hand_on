#
# ---------------------------------------------
# tmp102 with 0x49 slave address
# ---------------------------------------------
#
import bigSymbol
from machine import Pin, I2C
import ssd1306
import tmp102Class
import time

led = Pin(2, Pin.OUT, value=1)
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
dsp = bigSymbol.Symbol(oled)
t = tmp102Class.TMP102(0x49)

dsp.clear()
dsp.temp(0, 18)
t.sleep()

while True:
    led.value(0)
    dsp.text('{:0.2f}c'.format(t.one_shot_read_TempC()), 34, 18)
    oled.show()
    led.value(1)
    time.sleep(1)
