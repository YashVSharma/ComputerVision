
import cv2

print(cv2.__version__)
data='dog.JPG'

img=cv2.imread(data)
#img1=cv2.imread(data,0)
print(img)

cv2.imshow('window1',img)
cv2.imshow('window2',img-50)
cv2.imshow('window3',img[0:200,0:600]+100)
cv2.imshow('window4',img/2)
cv2.waitKey(0)