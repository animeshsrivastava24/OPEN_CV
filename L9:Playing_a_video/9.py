import numpy as np
import cv2
cap = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
#Playing a video is similar to use the camera , in place of camera index we have to pass the video file path with the name.
#While playing the video the waitKey() argument will should be around 25ms if it too low video will play too fast, if high then video will play slowly
#We must also get error due to wrong installation of ffmpeg or gstreamer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
"""This time we create a VideoWriter object. We should specify the output file name (eg: output.avi). Then we should
specify the FourCC code (details in next paragraph). Then number of frames per second (fps) and frame size should
be passed. And last one is isColor flag. If it is True, encoder expect color frame, otherwise it works with grayscale
frame.
FourCC is a 4-byte code used to specify the video codec. The list of available codes can be found in fourcc.org. It is
platform dependent. Following codecs works fine for me."""
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
  ret, frame = cap.read() 
  if ret==True:
     frame = cv2.flip(frame,0)
      # write the flipped frame
     out.write(frame)
     cv2.imshow('frame',frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
                             break
   else:
      break
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
