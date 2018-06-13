import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #hsv hue sat value
    lower_blue=np.array([0,180,100])
    upper_blue=np.array([255,255,255])

    #dark_blue=np.uint8([[[]]])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dialtion=cv2.dilate(mask,kernel,iterations=1)

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    #It is the difference between input and opening of image
    cv2.imshow("tophat",tophat)

    #it is the differnece between the closing of the input image and input image
    cv2.imshow('Blackhat',blackhat)





    
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dialtion',dialtion)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    k=cv2.waitKey(5) &0xFF
    if k==27:
        break
    

cv2.destroyAllWindows()
cap.release()
            
