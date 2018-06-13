import cv2
import numpy as np

# 500 x 250
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3=cv2.imread('pythonlogo.png')
#add=img1+img2

#add=cv2.add(img1,img2)#added all the pixel value together
weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)#giveing weightage to image values

#cv2.imshow('add',add)
cv2.imshow('weighted',weighted)

#rows,cols,channels=img3.shape
#roi=img1[0:rows,0:cols]
#img3gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
#ret,mask=cv2.threshold(img3gray,220,255,cv2.THRESH_BINARY_INV)

#cv2.imshow('mask',mask)

#mask_inv=cv2.bitwise_not(mask)

#img1_bg=cv2.bitwise_and(roi, roi, mask=mask_inv)
#img3_fg=cv2.bitwise_and(img3, img3, mask=mask)

#dst=cv2.add(img1_bg,img3_fg)
#img1[0:rows,0:cols]=dst

#cv2.imshow('res',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
