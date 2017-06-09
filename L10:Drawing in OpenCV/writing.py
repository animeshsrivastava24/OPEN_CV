
import numpy as np 
import cv2
#created a image
img=np.zeros((512,512,3),np.uint8)
# Draw a diagonal blue line with thickness of 5 px
img1 = cv2.circle(img,(447,63), 63, (0,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img1,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)
#now use a frame to show it just as displaying a image
cv2.imshow("Image",img1)
cv2.waitKey(0)           
cv2.destroyAllWindows()


