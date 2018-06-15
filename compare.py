import cv2
import numpy as np

img1 = cv2.imread('ShapeTestB4.png', 0)
img2 = cv2.imread('ShapeTestA.png', 0)
#img2 = cv2.imread('ShapeTestB3.png', 0)
img3 = cv2.imread('ShapeTestA3.png', 0)
img4 = cv2.imread('ShapeTestA4.png', 0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy,_ = cv2.findContours(thresh,1,1)
cnt1 = contours
contours,hierarchy,_ = cv2.findContours(thresh2,1,1)
cnt2 = contours

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print('1:',ret)

ret = cv2.matchShapes(cnt1,cnt2,2,0.0)
print('2:', ret)
ret = cv2.matchShapes(cnt1,cnt2,3,0.0)
print('3:', ret)

DST = cv2.addWeighted(img1,0.5,img2,0.5,0)
DST2 = cv2.addWeighted(DST, 0.5, img3, 0.5, 0)
DST3 = cv2.addWeighted(DST2, 0.5, img4, 0.5, 0)
cv2.imshow("Keypoints", DST3)
#cv2.waitKey(0)
