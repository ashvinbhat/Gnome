#use openCV to get only text from image and crop it accordingly

import cv2

img = cv2.imread('images/table.jpeg')

#convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('Output/testOut_grayScale.jpg', gray)

#threshold the image to get only black and white
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imwrite('Output/testOut_tresh.jpg', thresh)


