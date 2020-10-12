# from matplotlib import pyplot as plt
import numpy as np
from scipy import ndimage

# picture = plt.imread("greyscale_Coins.PNG")  # For debugging purposes.


def magnitude(x, y):  # Instead of supplying a magnitude function for matrices directly, use a function that takes input
    return np.sqrt((np.square(x) + np.square(y)))  # With magnitudes, square-root the sum of squares of x and y matrix.


def edge_enhance(img):  # An image argument, which will be a ndarray matrix will be used as the input for the function.

    f_x = np.array([[-1, 0, 1],  # Define a kernel for the partial derivative in the x-direction
                    [-2, 0, 2],
                    [-1, 0, 1]])
    f_y = np.array([[-1, -2, -1],  # Define a kernel for the partial derivative in the y direction
                    [0, 0, 0],
                    [1, 2, 1]])

    padding_scale = 1  # Set up how large the padding will be to allow gradient computation for edges.
    correction = padding_scale+1  # To allow the output image to write a value to a pixel; prevent matrix 'index errors'

    padded_image = np.pad(img, (padding_scale, padding_scale))  # Allows computation the gradient at boundaries
    output_image = np.zeros_like(img)  # Create an image output to allow a gradient to assign a value to each pixel

    print("Computing gradient of each pixel...")  # Indicate that the code is computing the gradient of each pixel.
    for y, column in enumerate(padded_image):  # Loop over each y pixel in the image to get its column.
        for x, value in enumerate(column):  # Loop over each x pixel in the image to get a value.
            if x == 0 or y == 0 or x == img.shape[1] - 1 or y == img.shape[0] - 1:
                continue  # Boundaries are not considered in the padded image
            else:
                window = padded_image[y - 1:y + 2, x - 1:x + 2]  # Create a 3x3 Matrix
                del_x = ndimage.convolve(window, f_x)  # Convolve the matrix with window and the y kernel in the x-dir
                del_y = ndimage.convolve(window, f_y)  # Convolve the matrix with window and the x kernel in the y-dir
                gradient = magnitude(np.sum(del_x), np.sum(del_y))  # Calculate the gradient of the two convolutions.
                output_image[y-correction][x-correction] = gradient # Set the value of output pixel to the gradient

    print("Gradient computation completed.")  # Indicate that the code has finished computation.
    return output_image  # Returns a Sobel-operated image matrix


# For debugging purposes
# new_pic = edge_enhance(picture)
# plt.imshow(new_pic, cmap="gray")
# plt.show()
