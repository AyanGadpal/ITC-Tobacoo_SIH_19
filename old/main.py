import numpy as np
from scipy import ndimage as ndi
import cv2
from skimage.filters import gabor_kernel

def compute_feats(image, kernels):
    feats = np.zeros((len(kernels), 2), dtype=np.double)
    for k, kernel in enumerate(kernels):
        filtered = ndi.convolve(image, kernel, mode='wrap')
        feats[k, 0] = filtered.mean()
        feats[k, 1] = filtered.var()
    return feats

def match(feats, ref_feats):
    min_error = np.inf
    min_i = None
    for i in range(ref_feats.shape[0]):
        error = np.sum((feats - ref_feats[i, :])**2)
        if error < min_error:
            min_error = error
            min_i = i
    return min_error

# prepare filter bank kernels
kernels = []
for theta in range(4):
    theta = theta / 4. * np.pi
    for sigma in (1, 3):
        for frequency in (0.05, 0.25):
            kernel = np.real(gabor_kernel(frequency, theta=theta,
                                          sigma_x=sigma, sigma_y=sigma))
            kernels.append(kernel)

# prepare reference features
devu_feats = np.zeros((20, len(kernels), 2), dtype=np.double)
manu_feats = np.zeros((20, len(kernels), 2), dtype=np.double)
ksku_feats = np.zeros((20, len(kernels), 2), dtype=np.double)
ayu_feats = np.zeros((20, len(kernels), 2), dtype=np.double)

for x in range(1,20):
    temp = cv2.resize(cv2.imread('new/Devu/' + str(x) + '.jpg',0),(600,800))
    devu_feats[x, :, :] = compute_feats(temp, kernels)

for x in range(1,20):
    temp = cv2.resize(cv2.imread('new/Manu/' + str(x) + '.jpg',0),(600,800))
    manu_feats[x, :, :] = compute_feats(temp, kernels)

for x in range(1,20):
    temp = cv2.resize(cv2.imread('new/Ksku/' + str(x) + '.jpg',0),(600,800))
    ksku_feats[x, :, :] = compute_feats(temp, kernels)

for x in range(1,20):
    temp = cv2.resize(cv2.imread('new/Ayu/' + str(x) + '.jpg',0),(600,800))
    ayu_feats[x, :, :] = compute_feats(temp, kernels)

feats = compute_feats(cv2.resize(cv2.imread('test/Devu/1.jpg',0),(600,800)),kernels)

mind = match(feats,devu_feats)
minm = match(feats,manu_feats)
mink = match(feats,ksku_feats)
mina = match(feats,ayu_feats)

print("Devu : " + str(mind))
print("Manu : " + str(minm))
print("Ksku : " + str(mink))
print("Ayu  : " + str(mina))

def power(image, kernel):   
    # Normalize images for better comparison.
    image = (image - image.mean()) / image.std()
    return np.sqrt(ndi.convolve(image, np.real(kernel), mode='wrap')**2 +
                   ndi.convolve(image, np.imag(kernel), mode='wrap')**2)