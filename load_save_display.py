# To run: python load_save_display.py --image <path-of-image>

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = ("Path to the image"))
args =  vars(ap.parse_args())
#Load
image = cv2.imread(args["image"]) #returns numpy array representing image
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channles: {}".format(image.shape[2]))
#Display
cv2.imshow("Image", image)
cv2.waitKey(0) #pauses execution until we press a key; 0 indicates any key press
#Save
cv2.imwrite("newimage.jpg", image)