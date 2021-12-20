#!/usr/bin/env python3

# -------------------------------------------------------------------
# Raspberry Pi + AM2320 + Adafruit IO 做一個遠端監看機房溫溼度的專案
# -------------------------------------------------------------------
# AM2320 -> RPi, 接4條線: I2C (Vcc, GND, SDA, SCL)
# 1. 先依以下網址安裝RPi的blinka程式界面:
# https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
# 2. 依以下網址安裝am2320 python 模組:
# https://learn.adafruit.com/adafruit-am2320-temperature-humidity-i2c-sensor/python-circuitpython
# 3. 在Adafruit IO 建立相對應的feeds: temperature, humidity

import time
import board
import busio
import adafruit_am2320
import paho.mqtt.publish as publish

# create the I2C shared bus
i2c = busio.I2C(board.SCL, board.SDA)
am = adafruit_am2320.AM2320(i2c)

# setting Adafruit IO
host = "io.adafruit.com"
topic_t = "poushen/feeds/temperature"
topic_h = "poushen/feeds/humidity"
payload = 27.4
auth = {'username':"你的帳號", 'password':"你的AIO KEY"}
client_id = "room/唯一編號(unique randon number)"

while True:
    humi = am.relative_humidity
    temp = am.temperature
    
    print('Humidity: {}%, Temperature: {}\u00B0C'.format(humi, temp))
    publish.single(topic_t, temp, qos=1, hostname=host, auth=auth, client_id=client_id)
    publish.single(topic_h, humi, qos=1, hostname=host, auth=auth, client_id=client_id)
    time.sleep(4)
    
