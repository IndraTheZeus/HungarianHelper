# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 20:51:22 2023

@author: indra
"""
from numpy import genfromtxt
from PIL import Image as im
import numpy as np
import os

DataDir = 'D:/Msc_DL_HungarianHelper/HungarianHelper/Data/bartosgye_ver6/'


my_data = genfromtxt('version6.txt', delimiter=',')
for featureClass in range(31, 40):
    my_classes = my_data[:,0] == featureClass
    my_class_data = my_data[my_classes,1:]
    print('Class: ', featureClass)
    print('Data Num:', my_class_data.shape)
    classDir = DataDir + str(featureClass - 4)
    if not os.path.exists(classDir): 
        os.makedirs(classDir) 
    for i in range(0,my_class_data.shape[0]):
        imgVec = my_class_data[i,:]
        im.fromarray(np.uint8(np.transpose(imgVec.reshape(28,28)))*255).save(classDir + '/img_' + str(i) + '.png')
