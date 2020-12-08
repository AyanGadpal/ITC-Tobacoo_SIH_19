# import the necessary packages
import cv2
import numpy as np
 
image = cv2.imread("a.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
temp = image.reshape((image.shape[0] * image.shape[1], 3))

rsum = np.sum(temp[:,0])
gsum = np.sum(temp[:,1])
bsum = np.sum(temp[:,2])

N = image[:,0].size

r = int(rsum/N)
g = int(gsum/N)
b = int(bsum/N)


# ======================= Manual ==============================
# sumrm = []
# for x in range(image[:,0].size):
#     sumrm.append(np.power(image[x,0],2))

# sumrm = np.asarray(sumrm)
# sumrm = np.sum(sumrm)
# sumrm = sumrm/N
# r2=r*r

# sdr = np.sqrt(sumrm-r2)
# print (sdr)
