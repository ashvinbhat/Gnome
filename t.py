#use Open CV to read the image

import cv2
import numpy as np

img = cv2.imread('Images1/labrep1_hack_camera2.jpeg')

#convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#threshold the image to get only black and white
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

cv2.imwrite('Output/testOut_grayScale.jpg', gray)
cv2.imwrite('Output/testOut_tresh.jpg', thresh)


#applying morphology to clean out the small regions of the image
kernel = np.ones((5,5), np.uint8)
img_erosion = cv2.erode(thresh, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

#find the contours and sort them by area and filter out the largest one
contours, hierarchy = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
cnt = contours[0]

#get the bounding box of the largest contour
x,y,w,h = cv2.boundingRect(cnt)

#draw the largest counter filled on a black background as a mask
mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, (255,255,255), -1)

#applying the mask to blacken out the background
res = cv2.bitwise_and(img, mask)

#crop the image to the bounding box
crop = res[y:y+h, x:x+w]


#save the image
cv2.imwrite('test.jpg', crop)


