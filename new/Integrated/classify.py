# import the necessary packages
import cv2
import numpy as np
from scipy import stats
import pickle

class Predictor:
    pickleout1 = None
    pickleout2 = None
    color_classifier = None
    ripeness_classifier = None

    def __init__(self):
        self.pickleout1 = open("ripenessclassifier.pickle","rb")
        u = pickle._Unpickler(self.pickleout1)
        u.encoding = 'latin1'
        self.ripeness_classifier = u.load()
        self.pickleout1.close()

        self.pickleout2 = open("colorclassifier.pickle","rb")
        u = pickle._Unpickler(self.pickleout2)
        u.encoding = 'latin1'
        self.color_classifier = u.load()
        self.pickleout2.close()
        
    # Method to calculate the ripeness features
    def calculate_feature_ripeness(self,image):
        image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        hist11 = cv2.calcHist([image],[0],None,[256],[0,256]).ravel()
        hist12 = cv2.calcHist([image],[1],None,[256],[0,256]).ravel()
        hist13 = cv2.calcHist([image],[2],None,[256],[0,256]).ravel()

        mean = cv2.mean(image)

        global_features = []
        global_features.append(mean[0])
        global_features.append(mean[1])
        global_features.append(mean[2])

        global_features.append(stats.mode(hist11)[0][0])
        global_features.append(stats.mode(hist12)[0][0])
        global_features.append(stats.mode(hist13)[0][0])

        global_features.append(stats.skew(hist11))
        global_features.append(stats.skew(hist12))
        global_features.append(stats.skew(hist13))

        global_features.append(stats.kurtosis(hist11))
        global_features.append(stats.kurtosis(hist12))
        global_features.append(stats.kurtosis(hist13))

        return np.asarray(global_features)

    # Method to calculate the color features
    def calculate_feature_color(self,image):
        hist11 = cv2.calcHist([image],[0],None,[256],[0,256]).ravel()
        hist12 = cv2.calcHist([image],[1],None,[256],[0,256]).ravel()
        hist13 = cv2.calcHist([image],[2],None,[256],[0,256]).ravel()

        mean = cv2.mean(image)

        global_features = []
        global_features.append(mean[0])
        global_features.append(mean[1])
        global_features.append(mean[2])

        global_features.append(np.std(hist11))
        global_features.append(np.std(hist12))
        global_features.append(np.std(hist13))

        return np.asarray(global_features)
    
    def make_prediction(self, imagefile):
        image = cv2.resize(cv2.imread(imagefile),(800,1200))
        feat1 = self.calculate_feature_color(image)
        feat2 = self.calculate_feature_ripeness(image)
        return self.color_classifier.predict(feat1.reshape(1,-1))[0],self.ripeness_classifier.predict(feat2.reshape(1,-1))[0]