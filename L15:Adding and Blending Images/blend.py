import numpy as np
import cv2
img1 = cv2.imread('/home/animesh/Desktop/1.png')
img2 = cv2.imread('/home/animesh/Desktop/2.png')
dst = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
