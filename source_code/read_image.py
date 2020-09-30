import cv2
import sys
img = cv2.imread(r'/images/image1.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()