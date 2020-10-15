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

    padding_scale = 1  # Set up how large the padding will be to allow gradient computation for edges
    correction = padding_scale + 1  # To allow the output image to write a value to a pixel; prevent matrix 'index errors'

    padded_image = np.pad(colorImage, (padding_scale, padding_scale))
    greyscaleImage = np.empty(colorImage.shape)

    print("Turning to grayscale...")
    for x_position, x in enumerate(colorImage):  # Enumerate the colorImage for indexing the row, x, for each row x
        for y_position, i in enumerate(x):  # Enumerate the colorImage for indexing the pixel, i, for each column y
            greyscaleImage[x_position, y_position] = 0.2126 * i[0] + 0.7152 * i[1] + 0.0722 * i[2]
            # calculated the greyscale value from each pixels rgb data

    # matplotlib.pyplot.imshow(greyscaleImage, cmap='gray', vmin=0, vmax=255)

    greyscaleImage = greyscaleImage[:, :, 0]

    print("Grayscale complete...")
    return greyscaleImage
