
import numpy as np 
import cv2
#created a image
img=np.zeros((512,512,3),np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img1 = cv2.circle(img,(447,63), 63, (0,0,255), -1)
#now use a frame to show it just as displaying a image
cv2.imshow("Image",img1)
cv2.waitKey(0)           
cv2.destroyAllWindows()


