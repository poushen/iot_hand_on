# get latest alarm value
# should be something like 1830

# how to enter new alarm value?
# go to website: https://dweet.io/play
# choise dweet POST /dweet/for/{thing}
#  thing : enter 'ops1234'
#  content: enter {"Alarm" : "1830"}

import urequests as req
import ujson

apiURL='{url}'.format(
    url='https://dweet.io/get/latest/dweet/for/ops1234'
)
r = req.get(apiURL)
obj = ujson.loads(r.text)

print('Alarm', obj['with'][0]['content']['Alarm'])
