from skimage import feature
import numpy as np
import cv2
import matplotlib.pyplot as plt

class LocalBinaryPatterns:
	def __init__(self, numPoints, radius):
		# store the number of points and radius
		self.numPoints = numPoints
		self.radius = radius
 
	def describe(self, image, eps=1e-7):
		# compute the Local Binary Pattern representation
		# of the image, and then use the LBP representation
		# to build the histogram of patterns
		lbp = feature.local_binary_pattern(image, self.numPoints,
			self.radius, method="uniform")

		cv2.imshow('original',image)
		cv2.imshow('lbp',lbp)
		cv2.waitKey(0)

		(hist, _) = np.histogram(lbp.ravel(),
			bins=np.arange(0, self.numPoints + 3),
			range=(0, self.numPoints + 2))
 
		# normalize the histogram
		hist = hist.astype("float")
		hist /= (hist.sum() + eps)
 
		# return the histogram of Local Binary Patterns
		return hist


desc = LocalBinaryPatterns(12, 4)

image = cv2.imread("no4.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hist = desc.describe(gray)

plt.plot(hist,'r-')
plt.ylabel('Feature Vectors')
plt.show()

