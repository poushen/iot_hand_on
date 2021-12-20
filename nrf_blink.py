from board import LED
from machine import RTCounter

def toggle_led(timer_id):
    LED(4).toggle()

rtc = RTCounter(1, period=5, mode=RTCounter.PERIODIC, callback=toggle_led)
rtc.start()