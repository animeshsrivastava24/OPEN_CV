import cv2
import numpy as np
# Load two images
img1 = cv2.imread('ralph.jpg')
img2 = cv2.imread('mainlogo.png')
#Now we want to remove the white background of the mainlogo and then place it on the top left of the 3D-Matplotlib (top coordinate's are (0,0)) So we will first find the coordinates y,x,channel of the mainlogo and then use it to reserve a region in ROI of 3D-Matplotlib image
#The shape of an image numpy array matrix tells us about its rows,coloumns and channels
#So uf we do img.shape we will get a tuple in return 
#And if find length of that tuple we will get the dimension the same answer using img.ndim
#So if we want to find value of no of rows ,coloumns and channels and store them in a value use
#row,colomns,channels=img.shape
rows,cols,channels = img2.shape
#So we found the area of img2
#Now we begin with the coordinate where we wannt to fit the image as [y,y+rows:x,x+cols] and here from (0,0) ,so
roi = img1[0:rows, 0:cols ]
#Now made a region in image1 
#Now we need to create a mask of the logo, mask is conversion to grayscale of an image
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) #color of image 2 converted to gray
#Now the image has a white background and rest thing we want to use and we dont need that white background so we select a threshold value say 220 generally things are white at this point and become more white till 255, if the background will have been yellow, we should have converted to gray so no need to worry about bckgrnd color coz we always convrt to gray .So we use the threshold value 220
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
#img2gray pixel whose value is above 220 is converted to 255 and whose value is below 220 is converted to black,after this we get a image and then invert the color 
#cv2.imshow("threshold inverted",mask) #To see the inverted image comment out
#now simply just create inverted image of mask
mask_inv = cv2.bitwise_not(mask)
#mask_inv=255-mask both are true 


#cv2.imshow("mask_inv",mask_inv)
# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
cv2.imshow("img1_bg",img1_bg)
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
cv2.imshow("img2_fg",img2_fg)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
#modify main image
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()
