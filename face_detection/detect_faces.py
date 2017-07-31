from __future__ import print_function
import argparse
from faceDetector import faceDetector
import cv2
import numpy as  np

ap= argparse.ArgumentParser()
ap.add_argument("-f","--face", required=True, help="path to face cascade")
ap.add_argument("-i","--image", required= True, help="path to image")
args= vars(ap.parse_args())
image= cv2.imread(args["image"])
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fd= faceDetector(args["face"])
# fd= faceDetector()
# print("Here")
faceRects= fd.detect(gray, scaleFactor=1.2, minNeighbors= 5, minSize=(30,30))
print("I found {} faces".format(len(faceRects)))

for(x,y,w,h) in faceRects:
	cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)