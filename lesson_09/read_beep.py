import mfrc522
from os import uname
from machine import Pin, PWM
import time

def do_read():

    beep = PWM(Pin(13), freq=1000)
    
    rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

    print("Place card before reader to read from address 0x08")

    try:
        while True:
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    beep.duty(900)
                    time.sleep(0.2)
                    beep.duty(0)
                    
                    print("New card detected")
                    print("  - tag type: 0x%02x" % tag_type)
                    print("  - uid   : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")

                    if rdr.select_tag(raw_uid) == rdr.OK:

                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]

                        if rdr.auth(rdr.AUTHENT1A, 8, key, raw_uid) == rdr.OK:
                            print("Address 8 data: %s" % rdr.read(8))
                            rdr.stop_crypto1()
                        else:
                            print("Authentication error")
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        beep.deinit()
        print("Bye")