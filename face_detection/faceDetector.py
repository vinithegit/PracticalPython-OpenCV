import cv2

class faceDetector:
	def __init__(self, faceCascadePath):
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self, image, scaleFactor=1.2, minNeighbors= 5, minSize=(30,30)):
		rects= self.faceCascade.detectMultiScale(image,
			scaleFactor= scaleFactor,
			minNeighbors= minNeighbors,
			minSize= minSize,
			flags= cv2.CASCADE_SCALE_IMAGE)
		return rects
