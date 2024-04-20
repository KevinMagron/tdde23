import cv2
import math

filename = "image.jpg"

image = cv2.imread("image.jpg")

def cvimg_to_list(picture):
    """Returns a list of every pixel's color value in tuples"""
    lst = []
    for y in range(picture.shape[0]):
        for x in range(picture.shape[1]):
            new_tuple = (image[y,x][0],image[y,x][1],image[y,x][2])
            lst.append(new_tuple)    
    return lst

def gaus(x,y):
    """Performs Gauss formula on given values x and y"""
    return -(1/(2*math.pi*(4.5**2)))*(math.e**(-((x**2) + (y**2))/(2 * (4.5**2))))

def unsharp_mask(n):
    """Returns a 2D list and performs Gauss formula on every square"""
    mask = [[gaus(x-n//2,y-n//2) for x in range(n)] for y in range(n)]
    mask[0][0] = 1.5
    return mask

