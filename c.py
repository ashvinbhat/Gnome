import cv2
import numpy as np

# read image as grayscale
img = cv2.imread('images/tt.jpeg')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# threshold
thresh = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)[1]\

# apply morphology
kernel = np.ones((7,7), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
kernel = np.ones((9,9), np.uint8)
morph = cv2.morphologyEx(morph, cv2.MORPH_ERODE, kernel)

# get largest contour
contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = contours[0] if len(contours) == 2 else contours[1]
area_thresh = 0
for c in contours:
    area = cv2.contourArea(c)
    if area > area_thresh:
        area_thresh = area
        big_contour = c


# get bounding box
x,y,w,h = cv2.boundingRect(big_contour)

# draw filled contour on black background
mask = np.zeros_like(gray)
mask = cv2.merge([mask,mask,mask])
cv2.drawContours(mask, [big_contour], -1, (255,255,255), cv2.FILLED)

# apply mask to input
result1 = img.copy()
result1 = cv2.bitwise_and(result1, mask)

# crop result
result2 = result1[y:y+h, x:x+w]

# save image
cv2.imwrite('testOut.jpg', result2)