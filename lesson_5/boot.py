# This file is executed on every boot (including wake-boot from deepsleep)

import esp
esp.osdebug(None)
import gc

def connectAP(ssid, pwd):
    import network
    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, pwd)
        while not wlan.isconnected():
            pass

    print('network config:', wlan.ifconfig())
    return wlan.ifconfig()[0]

# connect to your AP, change SSID, password
ip = connectAP('management', '12345678')

import webrepl
webrepl.start()
gc.collect()
