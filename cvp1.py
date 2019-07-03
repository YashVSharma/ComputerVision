#!/usr/bin/python
import cv2
import numpy as np
img1=cv2.imread('dog.JPG')
img2=cv2.imread('cat.jpg')
img3=img2[50:150,60:160]
img4=img1[50:150,60:160]
img1[50:150,60:160]=img3
img2[50:150,60:160]=img4


#img3=img1+img2
#img4=np.concatenate((img1,img2),axis=0)
#print(img1)
cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3',img3)
cv2.imshow('image4',img4)
cv2.waitKey(0)
