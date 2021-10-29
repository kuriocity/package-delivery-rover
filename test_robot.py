from bluedot import BlueDot
from gpiozero import Robot,DistanceSensor#,Servo
from time import sleep
robot1=Robot(left = (2,3), right = (17,27))
robot2=Robot(left = (5,6), right = (19,26))
robot3=Robot(left = (12,16), right = (20,21))
#robot1.backward()
#robot2.backward()
bd = BlueDot()
#sensor1 = DistanceSensor(echo=15, trigger=14)#-3 left
#sensor2 = DistanceSensor(echo=24, trigger=23)#-2 right

myCorrection1=0.47
maxPW1=(2.0+myCorrection1)/1000
minPW1=(1.0-myCorrection1)/1000
#myServo1 = Servo(9,min_pulse_width=minPW1,max_pulse_width=maxPW1)

myCorrection2=0.47
maxPW2=(2.0+myCorrection2)/1000
minPW2=(1.0-myCorrection2)/1000
#myServo2 = Servo(10,min_pulse_width=minPW2,max_pulse_width=maxPW2)

p=1
"""while True:
    print('Distance 1 : ', sensor1.distance * 100)
    print('Distance 2 : ', sensor2.distance * 100)
    print("-----------------------------------------------") 
    sleep(1)"""

"""while True: 
    robot1.forward()
    robot2.forward()
    print('Distance 1 : ', sensor1.distance * 100)
    print('Distance 2 : ', sensor2.distance * 100)
    print("-----------------------------------------------")
    sleep(1)
"""
"""while True:
    robot.forward()
    sleep(1)
    robot.stop()
    sleep(1)
    robot.right()
    sleep(1)
    robot.stop()
"""
def move(pos):
    if pos.top:
        robot1.forward()
        robot2.forward()
        robot3.forward()
        """while True:
            print("1=>"+str(sensor1.distance*100))
            print("2=>"+str(sensor2.distance*100))
            if(sensor1.distance*100 + 3)<=(30) or (sensor2.distance*100 + 2)<=(30):
                robot1.stop()
                robot2.stop()
                robot3.stop()
                print("obstacle")
                sleep(1)
            '''if(sensor1.distance*100 + 3)<=(30) and (sensor2.distance*100 + 2)<=(30):
                print(1)
            else:'''
            while sensor1.distance*100 + 3<=(33):
                robot1.right()
                robot2.right()
                robot3.right()
                if not bd.is_pressed:
                    break
            while sensor2.distance*100 + 2<=(33):
                robot1.left()
                robot2.left()
                robot3.left()
                if not bd.is_pressed:    
                    break
            if not bd.is_pressed:
                break
            robot1.forward(pos.distance)
            robot2.forward(pos.distance)
            robot3.forward(pos.distance)
            #else:
             #   robot1.forward(pos.distance)
             #   robot2.forward(pos.distance)
    
        '''elif bd.when_released:
             stop()'''
        '''robot1.forward(pos.distance)
        robot2.forward(pos.distance)'''
        print("up on"+str(pos.distance))"""
        
    elif pos.bottom:
        robot1.backward()
        robot2.backward()
        robot3.backward()
        print("down on"+str(pos.distance))
    elif pos.right:
        robot1.right()
        robot2.right()
        robot3.right()
        print("right on"+str(pos.distance))
    elif pos.left:
        robot1.left()
        robot2.left()
        robot3.left()
        print("left on"+str(pos.distance))

def stop():
    robot1.stop()
    robot2.stop()
    robot3.stop()
    p=0
    print("stop on")
bd.when_pressed = move
bd.when_moved = move
bd.when_released=stop
print("Last Line")

'''while True:
    robot1.forward()
    robot2.forward()
    if(sensor1.distance*100 + 3)<=(30): #or (sensor2.distance*100 + 2)<=(20):
        robot1.stop()
        robot2.stop()
        print("obstacle")        
        sleep(1)
        while sensor1.distance*100 + 3<=(30):
            robot1.right()
            robot2.right()
            sleep(0.1)
        #while sensor2.distance*100 + 2<=(20):
         #   robot1.left()
          #  robot2.left()        

'''
