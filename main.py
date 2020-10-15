"""
==========================================================================================================
ENGR 133 Fa 2020
GROUP 06
Dr. Eric Nauman
LC4-003

EDGE DETECTION PROJECT

Table "N" gineers

Authors:
Sihun Kim kim710@purdue.edu
Bill Lynch
Jacob Valdez valdez24@purdue.edu
Aidan Velleca avelleca@purdue.edu


==========================================================================================================
"""

'''
===============================================================================
ACADEMIC INTEGRITY STATEMENT
    [The team] has not used source code obtained from any other unauthorized
    source, either modified or unmodified. Neither has [the team] provided
    access to my code to another. The project [the team is] submitting
    is my own original work.
===============================================================================
'''

from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import numpy as np
import sys

from modules.edge_enhancement import edge_enhance
from modules.edge_detection import detectEdges
from modules.grayscale import Turn_Greyscale
from modules.noise_smoothing import noiseSmooth

image_directory = 'images/'
output_directory = 'output/'
output = '_output'
grey = '_grey'
blurred = '_blurred'
edged = '_edged'
detect = '_threshold'


try:
    image = input("Input the name of the file (without the extension) that you want to process: ")
    # Take in only the name of an existing file that exists in the
    extension = input("Input the extension of the file to process (e.g. png, jpg, bmp): ")
    imgFile = plt.imread(image_directory + image + '.' + extension)
except AttributeError:
    print(f"Error: The file must be an image. The following {image} is of type {type(image)}, which is a number")
    print("Exiting script...")
    sys.exit()
except FileNotFoundError:
    print(f"Error: File {image} cannot be found in the directory. Please input an existing file and try again.")
    print("Exiting script...")
    sys.exit()

try:
    threshold = int(input("Input an integer threshold between the range (0 to 100): ")) / 100
except ValueError:
    print(f"Error: The input must be a number")
    print("Exiting script...")
    sys.exit()

if threshold >= 1 or threshold <= 0:
    print("Error: The threshold must be within the range of 0 to 100.")
    print("Exiting script...")
    sys.exit()


def main():
    global imgFile  # Modify the imported image file globally, allowing exchange of processed images between functions.

    imgFile = Turn_Greyscale(imgFile)  # Turn the image greyscale.
    mpimg.imsave(output_directory + image + grey + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = noiseSmooth(imgFile)  # Noise smooth the image.
    mpimg.imsave(output_directory + image + blurred + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = edge_enhance(imgFile)  # Edge enhance the image
    mpimg.imsave(output_directory + image + edged + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = detectEdges(imgFile, threshold)  # Threshold the image for edges
    mpimg.imsave(output_directory + image + detect + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    plt.imshow(imgFile, cmap='gray')
    plt.show()

    mpimg.imsave(output_directory + image + output + '.' + extension, imgFile, cmap='gray', format='png')
    # Save the final, processed image into the output directory


if __name__ == '__main__':  # Because this is a script and not an executable, this statement is required.
    main()
