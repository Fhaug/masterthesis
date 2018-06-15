import cv2
import numpy as np

img1 = cv2.imread('A.jpg',0)
img2 = cv2.imread('B.jpg',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy,_ = cv2.findContours(thresh,2,1)
cnt1 = contours
contours,hierarchy,_ = cv2.findContours(thresh2,2,1)
cnt2 = contours

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)
cv2.imshow("Keypoints", img1)
cv2.waitKey(0)