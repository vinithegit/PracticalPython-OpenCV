import cv2
import argparse
ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args= vars(ap.parse_args())
image= cv2.imread(args["image"])
cv2.imshow("Original", image)
# cv2.waitKey(0)
# Flipping
flipped= cv2.flip(image, 1)
cv2.imshow("Flipped horizontally", flipped)
# cv2.waitKey(0)
flipped= cv2.flip(image, 0)
cv2.imshow("Flipped vertically", flipped)
# cv2.waitKey(0)
flipped=cv2.flip(image,-1)
cv2.imshow("flipped hori and vert", flipped)
cv2.waitKey(0)