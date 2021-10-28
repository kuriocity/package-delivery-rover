from gpiozero import *
from time import sleep

myGPIO=10

# Min and Max pulse widths converted into milliseconds
# To increase range of movement:
#   increase maxPW from default of 2.0
#   decrease minPW from default of 1.0
# Change myCorrection using increments of 0.05 and
# check the value works with your servo.
myCorrection=0.47
maxPW=(1.9+myCorrection)/1000
minPW=(0.9-myCorrection)/1000

#sensor1 = DistanceSensor(echo=24, trigger=23)
myServo = Servo(myGPIO,min_pulse_width=minPW,max_pulse_width=maxPW)
t=0.5

while True:
  myServo.mid()
  print("Set to middle position")
  sleep(t)
  #print("Distance :",sensor1.distance*100)
  sleep(0.5)
  myServo.min()
  print("Set to minimum position")
  sleep(t)
  #print("Distance :",sensor1.distance*100)
  sleep(0.5)
  myServo.mid()
  print("Set to middle position")
  sleep(t)
  #print("Distance :",sensor1.distance*100)
  sleep(0.5)
  myServo.max()
  print("Set to maximum position")
  sleep(t)
  #print("Distance :",sensor1.distance*100)
  sleep(0.5)

'''
while True:
  sum1=0
  c1=0
  print("Set value range -1.0 to +1.0")
  for value in range(0,21,2):
    value2=(float(value)-10)/10
    myServo.value=value2
    sleep(0.2)
    r1=sensor1.distance*100
    sum1+=r1
    c1+=1
    if value2==0:
      print("Average=",sum1/c1)
      sum1=0
      c1=0
    print("Servo value set to "+str(value2)+" Distance :"+str(r1))
    sleep(1)
  sum2=0
  c2=0
  print("Set value range +1.0 to -1.0")
  for value in range(20,-1,-2):
    value2=(float(value)-10)/10
    myServo.value=value2
    sleep(0.2)
    r2=sensor1.distance*100
    sum2+=r2
    c2+=1
    if value2==0:
      print("Average=",sum2/c2)
      sum2=0
      c2=0
    print("Servo value set to "+str(value2)+" Distance :"+str(r2))
    sleep(1)
'''
