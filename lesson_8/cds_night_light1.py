from machine import ADC, Pin
import time

ledPin = Pin(2, Pin.OUT)
adc = ADC(0)

while True:
    val = adc.read()

    if val >= 700:
        ledPin.value(0) # light on
    else:
        ledPin.value(1)        # light off

    time.sleep(0.5)
