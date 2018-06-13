import cv2
import numpy as np

img =cv2.imread('72 Alexandra Daddario Hot Beautiful Wide Screen Wallpapers (36).jpg',cv2.IMREAD_COLOR)

px=img[55,55]
print(px)

img[100:150, 100:150]=[255,255,255]
watch_face=img[37:111,107:194]
img[1:75,2:89]=watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
