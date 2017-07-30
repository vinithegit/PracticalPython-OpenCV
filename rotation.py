import cv2
import imutils
import numpy as np
import argparse
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image", required =True, help="Path to the image")
args= vars(ap.parse_args())
image= cv2.imread(args["image"])
cv2.imshow("Original",image)
cv2.waitKey(0)
(h,w)= image.shape[:2]
center= (w//2,h//2)
M= cv2.getRotationMatrix2D(center, 45, 1.0)
rotated= cv2.warpAffine(image, M, (w,h))
cv2.imshow("Rotated 45degrees", rotated)
cv2.waitKey(0)
M= cv2.getRotationMatrix2D(center, -90,1.0)
rotated= cv2.warpAffine(image,M, (w,h) )
cv2.imshow("Rotated by -90degrees", rotated)
cv2.waitKey(0)
rotated= imutils.rotate(image, 180)
cv2.imshow("Rotated by 180degrees", rotated)
cv2.waitKey(0)