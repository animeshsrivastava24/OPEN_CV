"""The codes here tell here how to access a pixel of an image and change its BGR values and various iamge attributes and how to find them using functions"""
import numpy as np
import cv2
a=cv2.imread('/home/animesh/Desktop/messi5.jpg',-1) #load a unchanged image so used -1
b=cv2.imread('/home/animesh/Desktop/messi5.jpg',0) #load a grayscale image so used 0
#The various methods to find the pixel location and then return the value of BGR value there is mentioned
#to access a pixel based on its row and coloumn location works on both color and grayscale

pix1=a[100,100]

pix2=b[100,100]
print 'BGR value of image' 
print pix1
print 'Intensity of Grayscale image'
print pix2
#Now what if we want specifially B(0), G(1) or R(2) value in a colored image
pix3=a[100,100,0]
pix4=a[100,100,1]
pix5=a[100,100,2]
#but the grayscale image can't be accessed like this it will show error
#Now what if we want to change values of a pixel simple find and replace
pix1=[30,14,20]
print pix1

#Numpy array methods using array.item() is used to access the same thing and
#array.itemset() is used to change the value of the scalar value returned by the array.item(), its shown below
pix6=a.item(100,100,0)
print pix6 #whatever it will return will be replaced by 100 in the next comnd
pix7=a.itemset((100,100,0),300)
print pix7 #if we print this it will return none becuase it has chnged the pixel value we need to print the new pix6
pix8=a.item(100,100,0)
print pix8
"""
Image properties include number of rows, columns and channels, type of image data, number of pixels etc.
Shape of image is accessed by img.shape. It returns a tuple of number of rows, columns and channels (if image is
color)"""
print a.shape
print b.shape
#Note: If image is grayscale, tuple returned contains only number of rows and columns. So it is a good method to
#check if loaded image is grayscale or color image.
#Total number of pixels is accessed by img.size:
print a.size
print b.size
#Image datatype is obtained by img.dtype
print a.dtype
