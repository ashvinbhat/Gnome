#use Open CV to read the image

import cv2
import numpy as np

img = cv2.imread('images/table.jpeg')

#convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#threshold the image to get only black and white
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

#applying morphology to clean out the small regions of the image
kernel = np.ones((7,7), np.uint8)
img_erosion = cv2.erode(thresh, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

#find the contours and sort them by area and filter out the smallest one
# contours, hierarchy = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = cv2.findContours(img_erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
# contours = sorted(contours, key=cv2.contourArea, reverse=True)
area_thresh = 0
for c in contours:
    area = cv2.contourArea(c)
    if area > area_thresh:
        area_thresh = area
        big_contour = c
cnt = big_contour

#get the bounding box of the smallest contour
x,y,w,h = cv2.boundingRect(cnt)

#draw the smalled counter filled on a black background as a mask
mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [cnt], 0, (255,255,255), -1)


#applying the mask to blacken out the background
res = cv2.bitwise_and(img, mask)

#crop the image to the bounding box
crop = res[y:y+h, x:x+w]

#save the image
cv2.imwrite('testOut1.jpg', crop)
