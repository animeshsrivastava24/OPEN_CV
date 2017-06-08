import numpy as np
import cv2
a=cv2.imread('/home/animesh/Desktop/messi5.jpg',1)
cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)
cv2.waitKey(0)
#The above program code create an empty window using cv2.namedWindow(). By default, the flag is
#cv2.WINDOW_AUTOSIZE i.e.We have to only create a window give its name and it has a second argument in which value is cv2.WINDOW_AUTOSIZE
#i.e. cv2.namedWindow('img', cv2.WINDOW_AUTOSIZE)= cv2.namedWindow('img'), the name AUTOSIZE is used because the window is so created that whenever we load any image in it, it gets automatically adjusted in the window
