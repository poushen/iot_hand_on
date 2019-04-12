from machine import ADC, Pin
from servo import Servo
import time

#ledPin = Pin(2, Pin.OUT)
adc = ADC(0)
s = Servo(0)
s.rotate(0)

while True:
    val = adc.read()

    if val < 200:
        s.rotate(90)
        time.sleep(0.5)
        s.rotate(0)
    else:
        pass

    time.sleep(0.5)