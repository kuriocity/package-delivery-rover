from datetime import datetime
import gpsd
from time import sleep
import requests
gpsd.connect()
received = False
avg=10
#print('%10.2f'%5.1234)
try:
    while True:
        sum1=0
        sum2=0
        for i in range(avg):
            gpsd.connect()
            packet = gpsd.get_current()
            pos1,pos2 = packet.position()
            print('%3.6f'%pos1,'%3.6f'%pos2)
            sum1+=pos1
            sum2+=pos2
            sleep(1)
        sum1=sum1/avg
        sum2=sum2/avg
        print("Latitude="+str('%3.6f'%sum1)+" Longitude="+str('%3.6f'%sum2))
 #received = True
except Exception:
    print("no signal")
''' 
if received == True:
 url = "https://google.com"
 lat = pos[0]
 lon =pos[1]
 tgl = datetime.now().strftime('%Y-%m-%d')
 wkt = datetime.now().strftime('%H:%M:%S')
 data = {'waktu':wkt, 'tanggal':tgl, 'lat':lat, 'lon':lon}
 r = requests.post(url=url, data=data)
 print (r.status_code)
'''
