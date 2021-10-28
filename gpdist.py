from gpiozero import DistanceSensor,Robot
from time import sleep
sensor1 = DistanceSensor(echo=15, trigger=14)
sensor2 = DistanceSensor(echo=24, trigger=23)
while True:
    print('Distance 1 : ', sensor1.distance * 100)
    print('Distance 2 : ', sensor2.distance * 100)
    print("-----------------------------------------------")
    sleep(1)
