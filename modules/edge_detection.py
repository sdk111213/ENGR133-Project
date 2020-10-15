# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 11:51:06 2020

@author: AIDAN
"""
from math import sqrt


# imgFile = plt.imread('Purdue_Arch.PNG')

# File should be Jake's output
def detectEdges(img, threshold):
    # Reads the image
    # img = plt.imread(imgFile)
    # Prints the dimensions of image
    print(f'Dimensions of the image is {img.shape}')

    # The new array for the edited image
    editedIm = img

    # row = 0

    # Reads each pixel and turns it to white or black based on its magnitude
    # Each row of pixels
    print('Comparing input threshold with pixel value')
    for row, i in enumerate(img):
        # Each pixel in row
        for pixel, j in enumerate(i):
            # Magnitude of the pixel
            clrMag = i[pixel]
            if clrMag < threshold:
                editedIm[row][pixel] = 0
            else:
                editedIm[row][pixel] = 1

    # Returns the edited image
    # newImg = plt.imshow(img, cmap='gray')
    return editedIm


# name = 'Coins.png'
# threshold = 0.65
# imgFile = detectEdges(imgFile, threshold)
