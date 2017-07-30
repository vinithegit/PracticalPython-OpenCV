from __future__ import print_function
import cv2
import mahotas
import numpy as np
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image", required= True, help="Path to image")
args=vars(ap.parse_args())
image= cv2.imread(args["image"])
image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

lap=cv2.Laplacian(image, cv2.CV_64F)
lap= np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)

sobelX= cv2.Sobel(image, cv2.CV_64F, 1,0)
sobelY= cv2.Sobel(image, cv2.CV_64F, 0,1)
sobelX= np.uint8(np.absolute(sobelX))
sobelY= np.uint8(np.absolute(sobelY))
sobelCombined= cv2.bitwise_or(sobelX, sobelY)
cv2.imshow("sobelX", sobelX)
cv2.imshow("sobelY", sobelY)
cv2.imshow("sobel combined", sobelCombined)
cv2.waitKey(0)
