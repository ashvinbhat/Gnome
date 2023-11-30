#crop image using open cv

import cv2
import numpy as np

#Read the input
img = cv2.imread('images/table.jpeg')

#Convert to grayscale  
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Threshold
ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)

#Apply morphology to clean it of small regions
kernel = np.ones((7,7), np.uint8)
img_erosion = cv2.erode(thresh, kernel, iterations=1)
img_dilation = cv2.dilate(img_erosion, kernel, iterations=1)

kernel = np.ones((7,7), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
kernel = np.ones((9,9), np.uint8)
morph = cv2.morphologyEx(morph, cv2.MORPH_ERODE, kernel)

#Get contours and filter to keep the largest one
# contours, hierarchy = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]
contours = sorted(contours, key=cv2.contourArea, reverse=True)
cnt = contours[0]

#Get the bounding box
x,y,w,h = cv2.boundingRect(cnt)

#Draw the largest contour filled on a black background as a mask
# mask = np.zeros(img.shape, np.uint8)
mask = np.zeros_like(gray)
mask= cv2.merge([mask, mask, mask])
# cv2.drawContours(mask, [cnt], 0, (255,255,255), -1)
cv2.drawContours(mask, [cnt], -1, (255,255,255), cv2.FILLED)

#apply mask to input
res1 = img.copy()
res1 = cv2.bitwise_and(res1, mask)


#Use the bounding box to crop the masked input
crop = res1[y:y+h, x:x+w]

#Save the image
cv2.imwrite('testOut.jpg', crop)

