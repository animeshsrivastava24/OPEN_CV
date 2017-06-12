import numpy as np
import cv2
im = cv2.imread('rectangle_canny.png')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#We want to know no. of boundary points stored.Since contour is a pyhton list containing boundary points as its element.
print contours
cnt = contours[0]
pni=cv2.drawContours(img, [cnt], 0, (0,255,0), 3)
cv2.imshow("pni",pni)
cv2.waitKey(0)
cv2.destroyAllWindows()
