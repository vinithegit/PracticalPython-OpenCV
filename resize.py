import numpy as np
import cv2
import argparse
import imutils
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args= vars(ap.parse_args())
image= cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
# Resizing over Width
r= 150.0/image.shape[1]
dim= (150, int(r*image.shape[0]))
resized= cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
cv2.imshow("Width resized", resized)
cv2.waitKey(0)
# Resizing over Height
r=50.0/image.shape[0]
dim=(int(r*image.shape[1]), 50)
resized= cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Height resized", resized)
cv2.waitKey(0)
#using imutils
resized= imutils.resize(image, width=100)
cv2.imshow("Resized imutils", resized)
cv2.waitKey(0)
resized= imutils.resize(image, height=50)
cv2.imshow("Resized imutils", resized)
cv2.waitKey(0)