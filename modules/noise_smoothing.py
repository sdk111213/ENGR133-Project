import numpy as np

def noiseSmooth(image): #the argument is the image converted into the array
    G = [[np.float(1),np.float(4),np.float(6),np.float(4),np.float(1)], #the 5x5 array containing the gaussian filter 
         [np.float(4),np.float(16),np.float(24),np.float(16),np.float(4)],
         [np.float(6),np.float(24),np.float(36),np.float(24),np.float(6)],
         [np.float(4),np.float(16),np.float(24),np.float(16),np.float(4)],
         [np.float(1),np.float(4),np.float(6),np.float(4),np.float(1)]]
                                                      
    z = np.zeros((len(image)+4,len(image[0])+4))  #creates a matrix of zeros that is zero padded with two additional columns and rows 
    blur = np.zeros((len(image),len(image[0]))) #creates the eventual matrix to return that is initially a matrix of zeros the size of the image 
    
    for x in range(0,len(image),1): #for the length of the image 
        for y in range(0,len(image[0]),1):  #for the height of the image 
            z[x+2][y+2] = image[x][y]  #assign the value of the image to the zero matrix at the two rows and two columns to the right and bottom because the zero matrix is bigger by four columns and four rows

    print('Edge Blurring/Noise smoothing...')
    for x in range(2,len(z)-4,1): #for the length of the zero padded matrix starting at the corner corresponding to the image 
        for y in range(2,len(z[0]) -4,1):#for the height of the zero padded matrix starting at the corner corresponding to the image #x is along row, y is along column 
            temp=[[z[x-2][y-2], z[x-1][y-2],z[x][y-2],z[x+1][y-2], z[x+2][y-2]],  #creates a temporary matrix that is the copy of the image 
                  [z[x-2][y-1],z[x-1][y-1],z[x][y-1], z[x+1][y-1], z[x+2][y-1]],
                   [z[x-2][y], z[x-1][y], z[x][y], z[x+1][y], z[x+2][y]],
                   [z[x-2][y+1], z[x-1][y+1], z[x][y+1], z[x+1][y+1], z[x+2][y+1]],
                   [ z[x-2][y+2],z[x-1][y+2], z[x][y+2], z[x+1][y+2], z[x+2][y+2]]]
            
            a = (temp[0][0]) * G[0][0]  #multiplies the image at the specific point with the corresponding value of the gaussian filter
            b = (temp[1][0]) * G[0][1]  #this is essentially the dot product of the vectors temp column 0 and row 0 
            c = (temp[2][0]) * G[0][2]
            d = (temp[3][0]) * G[0][3]       
            e = (temp[4][0]) * G[0][4]
            
            f = temp[0][1] * G[1][0]
            g = temp[1][1] * G[1][1]
            h = temp[2][1]* G[1][2]
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
        
            value = (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+xx+yy)/256.0 #sums the value and divides by 256
            blur[x-2][y-2] = value  #assigns the new image blurred image value at the point to the blurred matrix 
    print("Edge Blurring/Noise Smoothing Complete") #signals that the blurring is complete
    return blur  #returns blurred matrix

