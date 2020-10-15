import numpy as np

# o--========= Greyscale Image; written by Bill =========--o


def turn_greyscale(color_image):

    greyscale_image = np.empty(color_image.shape)

    print("Turning to grayscale...")
    for x_position, x in enumerate(color_image):  # Enumerate the colorImage for indexing the row, x, for each row x
        for y_position, i in enumerate(x):  # Enumerate the colorImage for indexing the pixel, i, for each column y
            greyscale_image[x_position, y_position] = 0.2126 * i[0] + 0.7152 * i[1] + 0.0722 * i[2]
            # calculated the greyscale value from each pixels rgb data

    greyscale_image = greyscale_image[:, :, 0]  # Remove the remaining RGB dimensions to convert it to greyscale.

    print("Grayscale complete...")
    return greyscale_image

# o--========= Noise smoothing; written by Sihun =========--o


def noise_smooth(image):  # the argument is the image converted into the array
    G = [[np.float(1), np.float(4), np.float(6), np.float(4), np.float(1)],
         # the 5x5 array containing the gaussian filter
         [np.float(4), np.float(16), np.float(24), np.float(16), np.float(4)],
         [np.float(6), np.float(24), np.float(36), np.float(24), np.float(6)],
         [np.float(4), np.float(16), np.float(24), np.float(16), np.float(4)],
         [np.float(1), np.float(4), np.float(6), np.float(4), np.float(1)]]

    # z = np.zeros((len(image)+4,len(image[0])+4))
    blur = np.zeros((len(image), len(
        image[0])))  # creates the eventual matrix to return that is initially a matrix of zeros the size of the image

    z = np.pad(image, (2, 2), mode='reflect') #creates a matrix of zeros that is zero padded with two additional columns and rows

    print('Edge Blurring/Noise smoothing...')
    for x in range(2, len(z) - 2,
                   1):  # for the length of the zero padded matrix starting at the corner corresponding to the image
        for y in range(2, len(z[0]) - 2,
                       1):  # for the height of the zero padded matrix starting at the corner corresponding to the image #x is along row, y is along column
            temp = [[z[x - 2][y - 2], z[x - 1][y - 2], z[x][y - 2], z[x + 1][y - 2], z[x + 2][y - 2]],
                    # creates a temporary matrix that is the copy of the image
                    [z[x - 2][y - 1], z[x - 1][y - 1], z[x][y - 1], z[x + 1][y - 1], z[x + 2][y - 1]],
                    [z[x - 2][y], z[x - 1][y], z[x][y], z[x + 1][y], z[x + 2][y]],
                    [z[x - 2][y + 1], z[x - 1][y + 1], z[x][y + 1], z[x + 1][y + 1], z[x + 2][y + 1]],
                    [z[x - 2][y + 2], z[x - 1][y + 2], z[x][y + 2], z[x + 1][y + 2], z[x + 2][y + 2]]]

            a = (temp[0][0]) * G[0][
                0]  # multiplies the image at the specific point with the corresponding value of the gaussian filter
            b = (temp[1][0]) * G[0][1]  # this is essentially the dot product of the vectors temp column 0 and row 0
            c = (temp[2][0]) * G[0][2]
            d = (temp[3][0]) * G[0][3]
            e = (temp[4][0]) * G[0][4]

            f = temp[0][1] * G[1][0]
            g = temp[1][1] * G[1][1]
            h = temp[2][1] * G[1][2]
            i = temp[3][1] * G[1][3]
            j = temp[4][1] * G[1][4]

            k = temp[0][2] * G[2][0]
            l = temp[1][2] * G[2][1]
            m = temp[2][2] * G[2][2]
            n = temp[3][2] * G[2][3]
            o = temp[4][2] * G[2][4]

            p = temp[0][3] * G[3][0]
            q = temp[1][3] * G[3][1]
            r = temp[2][3] * G[3][2]
            s = temp[3][3] * G[3][3]
            t = temp[4][3] * G[3][4]

            u = temp[0][4] * G[4][0]
            v = temp[1][4] * G[4][1]
            w = temp[2][4] * G[4][2]
            xx = temp[3][4] * G[4][3]
            yy = temp[4][4] * G[4][4]

            value = (
                a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + xx + yy
                    ) / 256.0  # sums the value and divides by 256
            blur[x - 2][y - 2] = value  # assigns the new image blurred image value at the point to the blurred matrix
    print("Edge Blurring/Noise Smoothing Complete")  # signals that the blurring is complete
    return blur  # returns blurred matrix

# o--========= Edge Enhance; written by Jacob =========--o


def magnitude(x, y):  # Instead of supplying a magnitude function for matrices directly, use a function that takes input
    return np.sqrt((np.square(x) + np.square(y)))  # With magnitudes, square-root the sum of squares of x and y matrix


def convolve_2d(w, k1, k2):  # Take a window matrix and two kernels as arguments; specialized for window, f_x, and f_y
    del_x = 0
    del_y = 0
    for y, column in enumerate(w):
        for x, value in enumerate(column):
            del_x += w[x] * k1[x]  # Convolve the matrix with window and the x kernel in the x-dir
            del_y += w[y] * k2[y]  # Convolve the matrix with window and the y kernel in the y-dir

    return del_x, del_y  # Return the gradient components


def edge_enhance(img):
    # An image, img, argument, which will be a ndarray matrix will be used as the input for the function

    f_x = np.array([[-1, 0, 1],  # Define a kernel for the partial derivative in the x-direction
                    [-2, 0, 2],
                    [-1, 0, 1]])
    f_y = np.array([[-1, -2, -1],  # Define a kernel for the partial derivative in the y direction
                    [0, 0, 0],
                    [1, 2, 1]])

    padding_scale = 3  # Set up how large the padding will be to allow gradient computation for edges
    correction = padding_scale+2  # To allow the output image to write a value to a pixel; prevent matrix 'index errors'

    padded_image = np.pad(img, (padding_scale, padding_scale), mode='reflect')  # Allows computation the gradient at boundaries
    output_image = np.zeros_like(img)  # Create an image output to allow a gradient to assign a value to each pixel

    print("Computing gradient of each pixel...")  # Indicate that the code is computing the gradient of each pixel
    for y, column in enumerate(padded_image):  # Loop over each y pixel in the image to get its column
        for x, value in enumerate(column):  # Loop over each x pixel in the image to get a value
            if x == 0 or y == 0 or x == padded_image.shape[1] - 1 or y == padded_image.shape[0] - 1:
                continue  # Boundaries are not considered in the padded image
            else:
                window = np.array(padded_image[y - 1:y + 2, x - 1:x + 2])  # Create a 3x3 Matrix
                del_x, del_y = convolve_2d(window, f_x, f_y)  # Transfer window operations from padded to output pixel
                gradient = magnitude(np.sum(del_x), np.sum(del_y))  # Calculate the gradient of the two convolutions
                output_image[y-correction][x-correction] = gradient  # Set the value of output pixel to the gradient

    print("Gradient computation completed.")  # Indicate that the code has finished computation

    return output_image  # Returns a Sobel-operated image matrix

# o--========= Threshold Edges; written by Aidan =========--o


def detect_edges(img, threshold):  # Takes a image matrix and a threshold float as an argument

    # Prints the dimensions of image
    print(f'Dimensions of the image is {img.shape}')

    # The new array for the edited image
    edited_image = img

    # Reads each pixel and turns it to white or black based on its magnitude
    # Each row of pixels
    print('Comparing input threshold with pixel value')
    for row, i in enumerate(img):
        # Each pixel in row
        for pixel, j in enumerate(i):
            # Magnitude of the pixel
            clr_mag = i[pixel]
            if clr_mag < threshold:
                edited_image[row][pixel] = 0
            else:
                edited_image[row][pixel] = 1

    # Returns the edited image
    return edited_image
