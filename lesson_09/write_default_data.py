import mfrc522
from os import uname

def do_write():

    rdr = mfrc522.MFRC522(0, 2, 4, 5, 14)

    print("")
    print("Place card before reader to write address 0x08")
    print("")

    try:
        while True:
            (stat, tag_type) = rdr.request(rdr.REQIDL)
            if stat == rdr.OK:
                (stat, raw_uid) = rdr.anticoll()
                if stat == rdr.OK:
                    print("New card detected")
                    print("  - tag type: 0x%02x" % tag_type)
                    print("  - uid   : 0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
                    print("")

                    if rdr.select_tag(raw_uid) == rdr.OK:

                        key = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
                        #key = [0xB0, 0xB1, 0xB2, 0xB3, 0xB4, 0xB5]
                        
                        # write block 8 with (00:00:...:00)
                        block = 0x08
                        if rdr.auth(rdr.AUTHENT1A, block, key, raw_uid) == rdr.OK:
                        #if rdr.auth(rdr.AUTHENT1B, block, key, raw_uid) == rdr.OK:
                            #stat = rdr.write(block, b"\xff\xff\xff\xff\xff\xff\xff\x07\x80\x79\xb0\xb1\xb2\xb3\xb4\xb5")
                            #stat = rdr.write(block, b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F")
                            stat = rdr.write(block, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
                            rdr.stop_crypto1()
                            if stat == rdr.OK:
                                print("Data written to card")
                            else:
                                print("Failed to write data to card")
                        else:
                            print("Authentication error")
                        '''
                        # write block B with (FF:FF...) default factory key
                        block = 0x0B
                        if rdr.auth(rdr.AUTHENT1A, block, key, raw_uid) == rdr.OK:
                        #if rdr.auth(rdr.AUTHENT1B, block, key, raw_uid) == rdr.OK:
                            stat = rdr.write(block, b"\xff\xff\xff\xff\xff\xff\xff\x07\x80\x69\xff\xff\xff\xff\xff\xff")
                            rdr.stop_crypto1()
                            if stat == rdr.OK:
                                print("Default key written to card")
                            else:
                                print("Failed to write default key to card")
                        else:
                            print("Authentication error")
                        '''
                    else:
                        print("Failed to select tag")

    except KeyboardInterrupt:
        print("Bye")
