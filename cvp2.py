import cv2
import numpy as np

img = cv2.imread('dog.jpg')
imgc = cv2.imread('cat.jpg')
img4=np.concatenate((img,imgc),axis=0)
img1=img[20:150,40:170]

res = cv2.resize(img1,None,fx=1.2, fy=1.2, interpolation = cv2.INTER_CUBIC)
print(res.shape)
img[20:176,40:196]=res
cv2.imshow('zoomed',res)
cv2.imshow('cropped',img1)
cv2.imshow('oiginal',img)
cv2.imshow('merged images',img4)

cv2.waitKey(0)