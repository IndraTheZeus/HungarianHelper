# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 15:36:45 2023

@author: indra
"""
import os
import random
import shutil
folders_list = ['bartosgye_ver1/', 'bartosgye_ver6/', 'challenge2/','icdar2003_chars/','icdar2003_chars_test/']
test_dir = 'Dataset/Test/'
train_dir = 'Dataset/Train/'
test_ratio = 0.2


charIndexes = {}
for i in range(1,71):
    charIndexes[i] = 0
    

testcharIndexes = {}
for i in range(1,71):
    testcharIndexes[i] = 0
    
for folder_name in folders_list:
    print('Processing Folder', folder_name)
    for class_name in os.listdir(folder_name):
        if os.path.isdir(folder_name + class_name):
            print('Processing class', class_name)
            curr_class = class_name
            image_list = os.listdir(folder_name + class_name)
            random.shuffle(image_list)
            train_list = image_list[:-round(len(image_list)*test_ratio)]  
            test_list = image_list[-round(len(image_list)*test_ratio):]
            print("Train images: ", str(len(train_list)), "Test Images: ", str(len(test_list)))
            for image_name in train_list:
                src = folder_name + class_name + '/' + image_name
                des = train_dir + class_name + '/' + str(charIndexes[int(class_name)]) + '.png'
                charIndexes[int(class_name)] = charIndexes[int(class_name)] + 1
                print('Copying', src, ' to ', des)
                if not os.path.exists(train_dir + class_name + '/'): 
                    os.makedirs(train_dir + class_name + '/') 
                shutil.copy(src, des)
            for image_name in test_list:
                src = folder_name + class_name + '/' + image_name
                des = test_dir + class_name + '/' + str(testcharIndexes[int(class_name)]) + '.png'
                testcharIndexes[int(class_name)] = testcharIndexes[int(class_name)] + 1
                print('Copying', src, ' to ', des)
                if not os.path.exists(test_dir + class_name + '/'): 
                    os.makedirs(test_dir + class_name + '/') 
                shutil.copy(src, des)