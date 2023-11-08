# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 15:02:15 2023

@author: indra
"""

import os
from PIL import Image 

textGT_dir = "Challenge2_Training_Task2_GT/"
imageGT_dir = "Challenge2_Training_Task12_Images/"
imageGT_ext = ".jpg"
charOut_dir = "HungarianHelper/Data/challenge2/"

charIndexes = {}
for i in range(1,71):
    charIndexes[i] = 0
def char2label(c):
    assert len(c) == 3
    ordinate = ord(c[1])
    if((ordinate >= 97) & (ordinate <= 122)):
        return (ordinate - 96)
    elif((ordinate >= 65) & (ordinate <= 90)):
        return (ordinate - 25)
    return -1


for filename in os.listdir(textGT_dir):
    if(filename[-3:] != 'txt'):
        continue
    print("Processing: ", filename)
    with open(textGT_dir + filename) as file:
        print("Opening image: " , imageGT_dir + (filename[:-7] + imageGT_ext))
        image = Image.open(imageGT_dir + filename[:-7] + imageGT_ext) 
        for line in file:
            print("Processing line: ", line)
            if(line == '\n'):
                continue
            linearr = str(line).split()
            if(len(linearr) != 10):
                continue
            character = linearr[-1]
            label = char2label(character)
            if(label == -1):
                continue
            des_path = charOut_dir + str(label) + "/"
            if not os.path.exists(des_path): 
                os.makedirs(des_path) 
            charImg = image.crop(tuple([int(x) for x in linearr[-5:-1]]))
            print("Saving character ", character, " :", (des_path +  str(charIndexes[label]) + ".png"))
            charImg.save(des_path +  str(charIndexes[label]) + ".png")
            charIndexes[label] = charIndexes[label] + 1
            
            
            
            
            
