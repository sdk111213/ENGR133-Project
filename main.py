from main_functions import detect_edges, edge_enhance, noise_smooth, turn_greyscale
from matplotlib import image as img  # Import matplotlib's image library to access a better image saving method
from matplotlib import pyplot as plt  # Import pyplot to extract a matrix out of the file image
import sys  # Import sys only for allowing a safe script exit.

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

    imgFile = turn_greyscale(imgFile)  # Turn the image greyscale.
    img.imsave(output_directory + image + grey + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = noise_smooth(imgFile)  # Noise smooth the image.
    img.imsave(output_directory + image + blurred + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = edge_enhance(imgFile)  # Edge enhance the image
    img.imsave(output_directory + image + edged + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = detect_edges(imgFile, threshold)  # Threshold the image for edges
    img.imsave(output_directory + image + detect + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    plt.imshow(imgFile, cmap='gray')
    plt.show()

    img.imsave(output_directory + image + output + '.' + extension, imgFile, cmap='gray', format='png')
    # Save the final, processed image into the output directory


if __name__ == '__main__':  # Because this is a script and not an executable, this statement is standard.
    main()
