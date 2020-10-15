from main_functions import detect_edges, edge_enhance, noise_smooth, turn_greyscale  # Import from main_functions.py
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

# The following string variables will be used for concatenating contextualized names into the image input
image_directory = 'images/'
output_directory = 'output/'
output = '_output'
grey = '_grey'
blurred = '_blurred'
edged = '_edged'
detect = '_threshold'

try:  # Wrap the input statement in try to catch errors
    image = input("Input the name of the file without the extension that you want to process (case-sensitive): ")
    # Take input only from name of an existing file that exists in the image folder, else FileNotFoundError
    extension = input("Input the extension of the file to process (e.g. png, jpg, bmp): ")
    # Input an appropriate extension of the existing file, else FileNotFoundError
    imgFile = plt.imread(image_directory + image + '.' + extension)
except AttributeError:
    # Catch an error if the following input is not an appropriate image file
    print(f"Error: The file must be an image. The following {image} is of type {type(image)}, which is a number")
    print("Exiting script...")
    sys.exit()
except FileNotFoundError:
    # Catch an error if the following concatenated inputs cannot be found in the image directory
    print(f"Error: File {image} cannot be found in the directory. Restart the script and try again.")
    print("Exiting script...")
    sys.exit()

try:
    threshold = int(input("Input an integer threshold between the range (0 to 100): ")) / 100
    # Take a user input threshold for the detect edges function and cast the input into an integer
except ValueError:
    # If the threshold input is a character that cannot be cast into an integer, catch a ValueError
    print(f"Error: The input must be a number. Restart the script and try again.")
    print("Exiting script...")
    sys.exit()

if threshold >= 1 or threshold <= 0:
    # If the threshold is not within the range, notify the user.
    print("Error: The threshold must be within the range of 0 to 100. Restart the script and try again.")
    print("Exiting script...")
    sys.exit()


def main():
    global imgFile  # Modify the imported image file globally, allowing exchange of processed images between functions.

    imgFile = turn_greyscale(imgFile)  # Turn the image greyscale.
    print("Saving greyscale image to a output folder...")
    img.imsave(output_directory + image + grey + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = noise_smooth(imgFile)  # Noise smooth the image.
    print("Saving noise-smoothed image to a output folder...")
    img.imsave(output_directory + image + blurred + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = edge_enhance(imgFile)  # Edge enhance the image
    print("Saving edge enhanced image to a output folder...")
    img.imsave(output_directory + image + edged + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    imgFile = detect_edges(imgFile, threshold)  # Threshold the image for edges
    print("Saving threshold processed image to a output folder...")
    img.imsave(output_directory + image + detect + '.' + extension, imgFile, cmap='gray', format='png')
    # Save this image step to an output directory

    print("Outputting image to a window...")
    plt.imshow(imgFile, cmap='gray')
    plt.show()

    print("Saving final processed image to a output folder...")
    img.imsave(output_directory + image + output + '.' + extension, imgFile, cmap='gray', format='png')
    # Save the final, processed image into the output directory


if __name__ == '__main__':  # Because this is a script and not an executable, this statement is standard for script exec
    main()
