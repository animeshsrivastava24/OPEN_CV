import numpy as np
import cv2
a=cv2.imread('/home/animesh/Desktop/messi5.jpg',1)
cv2.imshow('img',a)
#wait key function uses a argument say x , which denotes a millisecond, as name suggest it waits for x millisecond
#if within x millisecond a key is pressed then it returns the value of the key in integer form
#aLso if 0 is used as x then it waits indefinitely for any key to be pressed then next step of program occurs
cv2.waitKey(0)
cv2.destroyAllWindows()
