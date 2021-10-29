from gpiozero import Robot,DistanceSensor
from time import sleep
robot1=Robot(left = (2,3), right = (17,27))
while True:
        robot1.forward()
        sleep(1)
        robot1.backward()
        sleep(1)

print("test")
