# iot_hand_on

## 元培企管系物聯網實作課程  習作提要

### 參考用書

趙英傑, 超圖解Python物聯網實作入門, 旗標出版, 2018
```
https://swf.com.tw/?p=1129&fbclid=IwAR2Q0mU-z5KyP24LSUPYUlbB1Y1mwuI2pgoQH1HjX5JWm19o2rTcchT9Kwo
範例：http://www.flag.com.tw/DL.asp?FT797
```

### lesson_01
	
電腦環境設置與D1 Mini開發板韌體安裝
```
setup.txt  第一次做的程序
redo.txt  已做完燒錄MicroPyth韌體，重開機後做的程序
blink.py  閃爍LED的程式
```

### lesson_02

外加LED
```
blink2.py  閃爍外接LED的程式, 接D5
```

### lesson_03

AMPY工具程式的使用與按鈕開關
```
ampy.txt  AMPY工具的使用示範
button.txt  按鈕開關的程式
signal.txt  轉換訊號意義on -> off
touch.txt  觸控開關示範程式
```

### lesson_04

MicroPython語言基礎練習
```
function.txt  自訂函数
module.txt  自訂模組
list.txt  串列操作
tuple.txt  元組操作
dictionary.txt  字典操作
timer.txt  定時器操作
interrupt.txt  中斷操作
class.txt  類別操作
file.txt  檔案操作
my.py  自訂小工具
```

### lesson_05

D1 Mini Wifi使用與WEBREPL
```
webrepl.txt  WEBREPL啓用與使用
boot.py  開機自動執行程式，在此放置連AP基地台的設定
bytes.txt  資料型態bytes, bytearray的介紹，以及取得MAC位址的方法
```

### lesson_06

Serial interface (oneWire, UART, I2C, SPI)
```
one_wire.txt  單線通訊(dht11.py, ds18b20.py)
uart.txt  TXRX通訊(gps_test.py, test.py)
i2c.txt  I2C通訊(i2c_scan.py, diy12_1_3.py, oled.py, diy12_4.py)
bigSymbol.py  課本大字體程式
tmp102Class.py  TMP102驅動程式
tmp102_49.py  使用I2C位址0x49, 在OLED上顯示温度
max7219.py  MAX7219 LED點陣示範程式
spaceInvader.py  MAX7219顯示動畫
sdcard.py  SD卡模組
sdtest.py  在SD卡上讀寫資料的示範程式
adxl345_spi.py  ADXL345加速度計的驅動程式
adxl345_spi_test.py 讀取ADXL345加速度計值的示範程式
```

### lesson_07

PWM (pulse width modulation)
```
diy8_2.py  LED呼吸燈
diy9_1.py  救護車音效
diy9_3.py  音樂
background_play.py  不卡住播音樂
rotate_fun.py  伺服馬逹(Servo)轉動
servo.py  伺服馬逹驅動（封裝成類別）
dc_motor.txt  直流馬逹調速
```

### lesson_08

Analog Input
```
potentiometer.py  電位計
cds_night_light1.py  光敏電阻小夜燈1
cds_might_light2.py  光敏電阻小夜燈2
target.py  雷射槍玩具標靶
adxl335_x.py  讀取ADXL335加速度計單一軸的值
adxl335_xy_pcf8591.py  讀取ADXL335加速度計兩軸的值
motion_control_dc_motor.py  體感控制伺服馬逹
ads1x15-master  TI ADS1x15的驅動程式
ads1115_test2.py  ADS1115接TMP36
```

### lesson_09

RFID
```
micropython-mfrc522.txt  MFRC522讀卡機晶片驅動程式網址
read_beep.py  讀卡片UID及區塊#8, 成功時發出beep聲
read_beep2.py  讀卡片UID及區塊#8, 成功時發出beep聲，整理程式寫法
write_keyb.py  以出廠預設金鑰(FF:FF:FF:FF:FF:FF)改寫區段#2的金鑰B為(B0:B1:B2:B3:B4:B5)
write_data_using_keyb.py  以金鑰B寫入資料(00:01:...:0F)至區塊#8
write_default_data.py  將區塊#8內容寫成（00:00...:00)
weite_default_key.py  將區段#2的金鑰B改回出廠預設金鑰(FF:FF:FF:FF:FF:FF)
```

### lesson_11

Networking Basic
```
diy16_1  課本原本socket示範程式 (client.py, server.py)
diy16_1_fix 同上，但修正一些小問題
server_led.py  用socket來開關LED
diy16_2.py  讀取網頁的用戶端程式
diy16_2_1.py  同上, 但加上檢查是否已連網的檢查
https.py  讀取網頁的測試程式, 但使用https協定(而不是如diy16_2.py那樣使用http協定)
http_basic_ifttt.py  觸發IFTTT應用(Applet)Webhooks
```

### lesson_12

ESP8266 as Web Server and IoT Cloud(ThingSpeak)
```
diy17_1.py  只回應固定訊息的web server
diy17_2.py  動態回應當前温溼度的web server
diy17_2_fix.py  同上, 但修正一些小問題

可讀取網頁和圖檔的小型Web Server
http_file.py  網頁伺服器
www目錄  
  favicon.ico  圖示檔
  index.html  首頁
  img目錄
    python.png  影像檔
	
互動網頁界面的燈光調控器
diy17_5目錄
  webroot目錄
    favicon.ico  圖示檔
    index.html  首頁檔
  http_query.py 網頁伺服器
	
diy17_4_1.py  使用request物件(get方法)上傳資料至ThingSpeak
diy17_4_3.py  使用request物件(get方法)固定每20秒上傳DHT11温溼度資料至ThingSpeak
POST.py  使用request物件(post方法)上傳資料至ThingSpeak
```
