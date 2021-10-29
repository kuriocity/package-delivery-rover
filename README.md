# Package Delivery Rover :rocket:

This project is a prototype of **Self Driving Car**. It's based on embedded systems, to meet the current requirement of _delivery applications_ & to overcome the
problems of industrial automation. 

Here are a few outcomes which are successfully implemented
- The rover design made it possible to run over uneven surfaces.
- Obstacle avoidance mechanism avoids obstacles of considerable size.
- GPS module and Google Maps Api helps to find the trajectory.
- Security Mechanism ensures the package delivery only to the client.

## Photos of Robot

#### Rocker Bogie Design in Action

![Rocker Bogie Mechanism](/Photos/Rocker_Bogie.jpg)

#### Top View of Rover

![Top View](/Photos/Rocker_Bogie_Top_View.jpg)

## High Level Design

![High Level Design](/Photos/High_Level_Design.jpg)
## Flow Chart

#### This is the complete flow of how a user would interact with the rover

![Flow Chart](/Photos/flowchart.jpg)


## Idea (Concept)

- This Project is intended to deliver goods. It uses a GPS sensor and Google
Maps services or user defined map to deliver from a source to any destination.
- It uses an ultrasonic
distance sensor to map the surrounding to avoid obstacles and find the best route. It has versatile Wheels to run on uneven surfaces with a Structure robust enough and
powered with Lead Acid batteries. 
- All this system runs through Rasberry Pi and Arduino
Hardware with encoder motors to change directions on course.
- It is apparently intended
right now for small premises to deliver but this range can be extended far away.
- This project
can be modified more to suit environment by adding various sensors.
- Finally when the valuables are delivered,the client is prompted for password which is messaged to him to unlock and get hold of his delivery.
- Delivery being
the prime and promising objective,our application of Rover is not limited to it and is
highly versatile.

## Software

- The code is individually tested for all seperate hardware modules.
- All the different Python snippets when combined would make the project work with _hardware setup_.
- Please find the connections of different module wired pins & Raspberry Pie/Arduino inside the code itself!
- For Automated Emails, enter your Gmail Credentials inside the code.


## Hardware

- Raspberry Pi 3B+
- Arduino Uno
- Motor Driver(L298D)
- Micro Servo Motor
- PVC Pipes + other design-stuff like Wheels
- I2C LCD Backpack - PCF8574
- 4x3 Dial pad
- 12V Battery
- Neo GPS Module
- Ultrasonic Sensor HC-SR04
- Angle Sensor Mpu 9250  

