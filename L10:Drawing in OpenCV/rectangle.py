import numpy as np 
import cv2
#created a image
img=np.zeros((512,512,3),np.uint8)
"""" we will draw a green
rectangle at the top-right corner of image."""
img1= cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
#now use a frame to show it just as displaying a image
cv2.imshow("Image",img1)
cv2.waitKey(0)           
cv2.destroyAllWindows()

