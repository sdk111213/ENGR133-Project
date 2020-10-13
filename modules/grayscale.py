# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 10:59:55 2020

@author: billy
"""

import numpy as np
import matplotlib


def Turn_Greyscale(colorImage):
    # colorImage = matplotlib.pyplot.imread('Lenna_(test_image).png')
    # New array for storing the greyscale image data
    greyscaleImage = np.empty(colorImage.shape)
    yposition = 0  # Keeps track of the horizontal position when editing image data
    xposition = 0  # Keeps track of the vertical position when editing image data

    for x in colorImage:
        xposition = 0  # Resets the x position for every new row
        for i in x:
            greyscaleImage[yposition, xposition] = 0.2126 * i[0] + 0.7152 * i[1] + 0.0722 * i[
                2]  # calculated the greyscale value from each pixels rgb data
            xposition = xposition + 1
        yposition = yposition + 1  # Moves to the next row once every corresponding x position has been checked

    matplotlib.pyplot.imshow(greyscaleImage, cmap='gray', vmin=0, vmax=255)

    return (greyscaleImage)
