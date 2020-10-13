from matplotlib import pyplot as plt
import numpy as np
import sys

from modules.edge_enhancement import edge_enhance
from modules.edge_detection import detectEdges
from modules.grayscale import Turn_Greyscale
from modules.noise_smoothing import noiseSmooth

directory = 'images/'
output = '_output'

try:
    image = input("Input the name and extension (png, jpeg) of the file that you want to test: ")
    threshold = int(input("Input a threshold between the range (0 to 100): ")) / 100
except AttributeError:
    print(f"Error: The file must be an image. The following {image} is of type {type(image)}, which is a number")
    sys.exit()
except FileNotFoundError:
    print(f"Error: File {image} cannot be found in the directory. Please input an existing file and try again.")
    print("Exiting program...")
    sys.exit()

if threshold >= 100 or threshold <= 0:
    print("Error: The threshold must be within the range of 0 to 100.")

imgFile = plt.imread(directory + image)

imgFile = Turn_Greyscale(imgFile)

plt.imshow(imgFile, cmap='gray')
plt.show()

imgFile = noiseSmooth(imgFile)

plt.imshow(imgFile, cmap='gray')
plt.show()

imgFile = edge_enhance(imgFile)

plt.imshow(imgFile, cmap='gray')
plt.show()

imgFile = detectEdges(imgFile, threshold)

plt.imshow(imgFile, cmap='gray')
plt.show()

plt.imwrite(imgFile, image + output, 'png')
