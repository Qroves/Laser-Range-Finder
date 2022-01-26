## program written by Shane Ormonde 7th sept 2013
## updated on 25th January 2014
## calculates the distance of a red dot in the field of view of the webcam.


import cv2
from numpy import *
import math

#variables
loop = 1

dot_dist = 0

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)



if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
	
else:
    rval = False
    #print "failed to open webcam"
	

if rval == 1 :

	while loop == 1:
			cv2.imshow("preview", frame)
			rval, frame = vc.read()
			key = cv2.waitKey(20)
			if key == 27: # exit on ESC
				loop = 0
			num = (frame[:,:,2] > 236)
			xy_val =  num.nonzero()

			y_val = median(xy_val[0])
			x_val = median(xy_val[1])

			dist = ((x_val - 320)**2 + (y_val - 240)**2 )**0.5 # distance of dot from center pixel
			#dist = abs(x_val - 320) # distance of dot from center x_axis only
			
			print (" dist from center pixel is " + str(dist))	
			
			# work out distance using D = h/tan(theta)
			
			theta =0.0011450*dist + 0.0154         
			tan_theta = math.tan(theta)
			
			

			if tan_theta > 0: # bit of error checking
				obj_dist =  int(5.33 / tan_theta)
			
			
			print ("\033[12;0H" + "the dot is " + str(obj_dist) + "cm  away")
elif rval == 0:
		print (" webcam error ")