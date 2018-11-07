import init_library as robot  #Library tha handles all the serial commands to arduino AtMega
import time
import numpy as np


robot.enablePID(1) #Enables PI (Proportional Integral) on robot this causes two things, we no longer can send regular robot.motors() commands because PI will immedietly 0 them. It allows us to use motorsRPM command which is regulated by our PI loop


robot.motorsRPM(0,0,0) #This takes a rpm value for example robots.motorsRPM(180,0,0) would make wheel one rotate 180 times a min. I'd leave this here as it makes sure your motors are off at start and this can be helpful (max right now is around 180RPM)

#robot.RPM(0) reads motor 0's rpm. 
print(robot.RPM(0))


#you can use this function to implement your inverse kinematic equations to calculate a RPM value to give the robot. Essentially your xd (x dot a.k.a x velocity) will be the value you pass in to move the robot in the x direction in meters per second. The same applies to yd. thetad will be your orientation and is in radians, for example 3.14 would be half a rotation a second.
def kinematic(xd,yd,thetad):
	r = 0.03 # radius of each wheel [m]
	l = 0.19 # distance from each wheel to the point of reference [m]
 
	
	print(wheel0RPM)
	print(wheel1RPM)
	print(wheel2RPM)

	robot.motorsRPM(wheel0RPM,wheel1RPM,wheel2RPM) 

#just a simple way to test your kinematic equation feel free to change it to your need, should work fine if you implement kinematic correctly. 
mode = input("Do you want to test your kinematic equation? [y/n] ")

if mode == 'y' or mode == 'Y':
	while True:
		x = float(input("enter desired x velocity (max .5 m/s): "))
		y = float(input("enter desired y velocity (max .5 m/s): "))
		theta = float(input("enter desired angular velocity (max π rad/s): "))
		mytime  = float(input("enter time to run: "))
		kinematic(x,y,theta)
		
		time.sleep(mytime)
		
		robot.motorsRPM(0,0,0)


robot.motorsRPM(0,0,0)
