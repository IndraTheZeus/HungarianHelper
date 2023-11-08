# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:36:46 2023

@author: indra
"""
import xml.etree.ElementTree as ET
import shutil
import os

# Define the XML file path
xml_file = "D:\Msc_DL_HungarianHelper\char\char.xml"
source_dir = "D:/Msc_DL_HungarianHelper/char/"
des_dir = "D:/Msc_DL_HungarianHelper/HungarianHelper/Data/icdar2003_chars_test/"


charIndexes = {}
for i in range(1,71):
    charIndexes[i] = 0
    
def char2label(c):
    assert len(c) == 1
    ordinate = ord(c)
    if((ordinate >= 97) & (ordinate <= 122)):
        return (ordinate - 96)
    elif((ordinate >= 65) & (ordinate <= 90)):
        return (ordinate - 25)
    return -1


# Create an empty dictionary to store the data
image_data = {}

# Parse the XML file
tree = ET.parse(xml_file)
root = tree.getroot()

# Iterate through the 'image' elements and extract the data
for image_elem in root.findall(".//image"):
    file_name = image_elem.get("file")
    tag = image_elem.get("tag")
    print('Processing file:', file_name, " : ", tag)
    label = char2label(tag)
    if(label == -1):
        continue
    src = source_dir + file_name
    des = des_dir + str(label) + "/" + str(charIndexes[label]) + ".png"
    charIndexes[label] = charIndexes[label] + 1
    if not os.path.exists(des_dir + str(label) + "/"): 
        os.makedirs(des_dir + str(label) + "/") 
    print("Copying ", src, ' to ', des)
    shutil.copy(src, des)
    

# Print the resulting dictionary
print(image_data)