# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils1
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())

# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(args["image"])

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# show our image
#plt.figure()
#plt.axis("off")
#plt.imshow(image)
#plt.show()
image = image.reshape((image.shape[0] * image.shape[1], 3))
print(image)
clt = KMeans(n_clusters = args["clusters"])
clt.fit(image)



hist = utils1.centroid_histogram(clt)
bar = utils1.plot_colors(hist, clt.cluster_centers_)
 
# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()
