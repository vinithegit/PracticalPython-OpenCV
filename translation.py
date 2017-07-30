from __future__ import print_function
import cv2
import imutils
import argparse
import numpy as np
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help= "Path to the image")
args= vars(ap.parse_args())
image= cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)
M= np.float32([[1,0,25],[0,1,50]])
shifted= cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted down and right", shifted)
cv2.waitKey(0)
M= np.float32([[1,0,-50],[0,1,-90]])
shifted= cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted up and left", shifted)
cv2.waitKey(0)
shifted= imutils.translate(image, 0,100)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)