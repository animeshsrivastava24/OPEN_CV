import numpy as np
import cv2
#Create a VideoCapture object that is used to capture frame by frame because video is a combination of images
cap = cv2.VideoCapture(0)
#We always need to check whether our 'cap' object created above is initialized or not, sometime cap used is not initialized and we may get an 
#error.So we can check whether it is open or not by cap.isOpened() which will return a boolean true/false, if it is false we can use cap.open(#pass 0 here if we want to initialize it for laptop integrated cam)
cap.open(0)
print cap.isOpened()
while(True):
# Capture frame-by-frame
	ret, frame = cap.read()
#here frame is used to get to the next frame in the camera (via 'cap').'ret' will obtain return value from getting camera frame, ret returns boolean value, it tells us if frame is returned or not
        print ret
        print frame
# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# Display the resulting frame
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
