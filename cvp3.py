#!/usr/bin/python
import cv2
import numpy as np
img1=cv2.imread('dog.JPG')
img2=cv2.imread('cat.jpg')
img3=img1+img2
img6=img1-img2

img5=cv2.absdiff(img1,img2)

cv2.imshow('image addition',img3)
cv2.imshow('image subtration',img6)
cv2.imshow('diff b/w 2 imgs',img5)
cv2.waitKey(0)

