"""What if we want to create two window image and destroy only one of it"""
import numpy as np
import cv2
#We have used while loop for img and img1 window to wait for us to press key a
a=cv2.imread('/home/animesh/Desktop/messi5.jpg',1)
cv2.imshow('img',a)
cv2.imshow('img1',a)
while 1:
	#wait key function uses a argument say x , which denotes a millisecond, as name suggest it waits for x millisecond
	#if within x millisecond a key is pressed then it returns the value of the key in integer form
	#aLso if 0 is used as x then it waits indefinitely for any key to be pressed then next step of program occurs
#Here we have created a destroyWindow program only for one window named 'img'
  if cv2.waitKey(1) & 0xFF==27 :
                        cv2.destroyWindow('img')				
			break
#This wait key for all windows in general
cv2.waitKey(0)

