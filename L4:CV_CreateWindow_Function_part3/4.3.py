"""Here we will create a window whose size can be controlled and changed, if we specify flag to be cv2.WINDOW_NORMAL, you can resize window. It will be
helpful when image is too large in dimension and adding track bar to windows."""
import numpy as np
import cv2
a=cv2.imread('/home/animesh/Desktop/messi5.jpg',1)
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
#We created a blank window using above code now its name is img
#So if we want to add image in it use the same name
cv2.imshow('img',a)
cv2.waitKey(0)

