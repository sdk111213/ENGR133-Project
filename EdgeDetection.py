# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:51:06 2020

@author: AIDAN
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# File should be Jake's output
def detectEdges(imgFile, threshold):
    # Reads the image
    img = plt.imread(imgFile)
    # Prints the dimensions of image
    print(f'Dimensions of the image is {img.shape}')
    # Converts image to array
    imArr = np.array(img)
    
    # The new array for the edited image
    editedIm = imArr
    
    row = 0
    
    # Reads each pixel and turns it to white or black based on its magnitude
    # Each row of pixels
    for i in imArr:
        pixel=0
        # Each pixel in row
        for j in i:
            #Magnitude of the pixel
            clrMag = sqrt(pow(j[0],2) + pow(j[1],2) + pow(j[2],2))
            if clrMag < threshold:
                editedIm[row][pixel] = [0, 0, 0, 1]
            else:
                editedIm[row][pixel] = [1, 1, 1, 1]
            pixel += 1
        row += 1
    
    # Returns the edited image
    newImg = plt.imshow(editedIm, cmap='gray')
    
name = 'Coins.png'
threshold = 0.65
detectEdges(name, threshold)
