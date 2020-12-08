# import the necessary packages
import cv2
import numpy as np
from scipy import stats
import imutils

class Segmentor:
    def segment(self, image):
        img = image.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.GaussianBlur(image, (3, 3), 0)
        image = cv2.Canny(image, 30, 185)
        image = cv2.dilate(image,None,iterations=5)
        image = cv2.erode(image,None,iterations=4)
        cnts = cv2.findContours(image, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(image.shape[:2], dtype="uint8") * 255
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cv2.drawContours(mask, cnts, -1, 255, -1)
        img = cv2.bitwise_and(img, img, mask=mask)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        img[np.all(img == [0, 0, 0, 255], axis=2)] = [0, 0, 0, 0]
        return img
# def match(feats, ref_feats):
#     min_error = np.inf
#     min_i = None
#     for i in range(ref_feats.shape[0]):
#         error = np.sum((feats - ref_feats[i, :])**2)
#         if error < min_error:
#             min_error = error
#             min_i = i
#     return min_error

seg = Segmentor()

image = cv2.resize(cv2.imread("16.jpg"),(400,600))
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image = seg.segment(image)
cv2.imshow("im1",image)
hist11 = cv2.calcHist([image],[0],None,[256],[0,256]).ravel()
hist12 = cv2.calcHist([image],[1],None,[256],[0,256]).ravel()
hist13 = cv2.calcHist([image],[2],None,[256],[0,256]).ravel()
# image = image.reshape((image.shape[0] * image.shape[1], 3))

image1 = cv2.resize(cv2.imread("19.jpg"),(400,600))
# image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
# image1 = seg.segment(image1)
cv2.imshow("im2",image1)
hist21 = cv2.calcHist([image1],[0],None,[256],[0,256]).ravel()
hist22 = cv2.calcHist([image1],[1],None,[256],[0,256]).ravel()
hist23 = cv2.calcHist([image1],[2],None,[256],[0,256]).ravel()
# image1 = image1.reshape((image1.shape[0] * image1.shape[1], 3))

# print(hist11.ravel())
global_features = []
global_features.append([])

global_features[0].append(np.mean(hist11))
global_features[0].append(np.mean(hist12))
global_features[0].append(np.mean(hist13))

# global_features[0].append(np.mean(image[:,0]))
# global_features[0].append(np.mean(image[:,1]))
# global_features[0].append(np.mean(image[:,2]))

# N = image[:,0].size
# r = int(rsum/N)
# g = int(gsum/N)
# b = int(bsum/N)
# print(np.std(image[:,0]))
# print(np.std(image[:,1]))
# print(np.std(image[:,2]))

global_features.append([])
global_features[1].append(stats.mode(hist11)[0][0])
global_features[1].append(stats.mode(hist12)[0][0])
global_features[1].append(stats.mode(hist13)[0][0])

global_features.append([])
global_features[2].append((np.std(hist11) * np.std(hist11)/1000))
global_features[2].append((np.std(hist12) * np.std(hist12)/1000))
global_features[2].append((np.std(hist13) * np.std(hist13)/1000))

global_features.append([])
global_features[3].append(stats.skew(hist11))
global_features[3].append(stats.skew(hist12))
global_features[3].append(stats.skew(hist13))

global_features.append([])
global_features[4].append(stats.kurtosis(hist11))
global_features[4].append(stats.kurtosis(hist12))
global_features[4].append(stats.kurtosis(hist13))

print(global_features[0])
print(global_features[1])
print(global_features[2])
print(global_features[3])
print(global_features[4])


# ===================================================================
# ===================================================================
# ===================================================================
# ===================================================================

global_features1 = []
global_features1.append([])
print(hist12.sum())
print(hist22.sum())

global_features1[0].append(np.mean(hist21))
global_features1[0].append(np.mean(hist22))
global_features1[0].append(np.mean(hist23))

# N = image[:,0].size
# r = int(rsum/N)
# g = int(gsum/N)
# b = int(bsum/N)
# print(np.std(image[:,0]))
# print(np.std(image[:,1]))
# print(np.std(image[:,2]))

print('')
print('')
print('')

global_features1.append([])
global_features1[1].append(stats.mode(hist21)[0][0])
global_features1[1].append(stats.mode(hist22)[0][0])
global_features1[1].append(stats.mode(hist23)[0][0])

global_features1.append([])
global_features1[2].append((np.std(hist21) * np.std(hist21))/1000)
global_features1[2].append((np.std(hist22) * np.std(hist22))/1000)
global_features1[2].append((np.std(hist23) * np.std(hist23))/1000)

global_features1.append([])
global_features1[3].append(stats.skew(hist21))
global_features1[3].append(stats.skew(hist22))
global_features1[3].append(stats.skew(hist23))

global_features1.append([])
global_features1[4].append(stats.kurtosis(hist21))
global_features1[4].append(stats.kurtosis(hist22))
global_features1[4].append(stats.kurtosis(hist23))

print(global_features1[0])
print(global_features1[1])
print(global_features1[2])
print(global_features1[3])
print(global_features1[4])


print('')
print('')
print('')

print(np.asarray(global_features))
# print(np.mean(np.asarray(global_features) - np.asarray(global_features1)))
print(np.sqrt(np.sum((np.asarray(global_features) - np.asarray(global_features1)) ** 2)))
# print("R")
# print((np.std(image[:,0])/r) * 100)
# print("G")
# print((np.std(image[:,1])/g) * 100)
# print("B")
# print((np.std(image[:,2])/b) * 100)

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

cv2.waitKey(0)