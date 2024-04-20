import cv2
import math
import lab5a
import cvlib
import random
import numpy

plane_img = cv2.imread("image.jpg")
flowers_img = cv2.imread("flowers.jpg")
gradient_img = cv2.imread("gradient.jpg")


def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """Checks if hsv-values are in given interval"""
    if not all(0 <= val <= 255 for val in [hlow, hhigh, slow, shigh, vlow, vhigh]):
        raise ValueError("Arguments must be valid hsv-values")
    
    def is_hsv(hsv_pixel):
        if not isinstance(hsv_pixel, tuple) or len(hsv_pixel) != 3:
            raise TypeError("Pixel_constraint recieved unexpected input.")
        hue, saturation, value = hsv_pixel
        if not (isinstance(hue, numpy.uint8) and isinstance(saturation, numpy.uint8) and isinstance(value, numpy.uint8)):
            raise TypeError("Pixel_constraint recieved unexpected input.")
        if not (0 <= hue <= 255 and 0 <= saturation <= 255 and 0 <= value <= 255 ):
            raise ValueError("Pixel_constraint recieved unexpected input.")
        return 1 if (hlow <= hue <= hhigh and slow <= saturation <= shigh and vlow <= value <= vhigh) else 0

    return is_hsv

def generator_from_image(lst_image):
    """Takes in a picture as a list and indexes it"""
    def generator(index):
        if index >= len(lst_image):
            raise IndexError("Index out of range in generator_from_image")
        return image_list[index]

    return generator


gradient_img_list = lab5a.cvimg_to_list(gradient_img)
image_img_list = lab5a.cvimg_to_list(plane_img)
flowers_img_list = lab5a.cvimg_to_list(flowers_img)

generator_flowers = generator_from_image(flowers_img_list)
generator_plane = generator_from_image(image_img_list)

def combine_images(lst, cond, gen1, gen2):
    """Takes in an image as a list and combines 2 other images in every pixel"""
    new_list = []
    try:
        for i,elem in enumerate(lst):
            new_list.append(cvlib.add_tuples((cvlib.multiply_tuple(gen1(i),cond(elem))), (cvlib.multiply_tuple(gen2(i),1-cond(elem))))) 
    except IndexError:
        raise IndexError("Images must have the same size")
    except ValueError:
        raise ValueError("Index out of range")
    except TypeError:
        raise TypeError("Index must be an integer")
    return new_list

def gradient_condition(tuple):
    """Takes in gray-scale tuples and returns a value from 0 to 1 depending on how white/dark image is"""
    return tuple[2]/255

result = combine_images(gradient_img_list, gradient_condition, generator_flowers, generator_plane)

new_img = cvlib.rgblist_to_cvimg(result, flowers_img.shape[0], flowers_img.shape[1])
cv2.imshow('Final image', new_img)
cv2.waitKey(0)




# generator_test = generator_from_image([(255,255,255),(128,128,128),(0,0,0)])
# generator_test2 = generator_from_image([(0,0,0),(128,128,128),(255,255,255)])

# test_result = combine_images(((255,255,255), (128,128,128), (255,255,255)), gradient_condition, generator_test, generator_test2)
# print(test_result)

# image = cv2.imread("magei.jpg")

# cv2.imshow('Morgan', image)

# is_black = pixel_constraint(0, 255, 0, 255, 0, 10)

# hsv_plane = cv2.cvtColor(cv2.imread("image.jpg"), cv2.COLOR_BGR2HSV)
# plane_list = lab5a.cvimg_to_list(hsv_plane)

# is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
# sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

# cv2.imshow('sky', cvlib.greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
# cv2.waitKey(0)

# orig_img = cv2.imread("image.jpg")
# orig_list = lab5a.cvimg_to_list(orig_img)

# generator = generator_from_image(orig_list)

# condition = pixel_constraint(100, 150, 50, 200, 100, 255)

# new_list = [generator(i) for i in range(len(orig_list))]

# cv2.imshow('original', orig_img)
# cv2.imshow('new', cvlib.rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))

# Skapa en generator som gör en stjärnhimmel
# def generator1(index):
#     val = random.random() * 255 if random.random() > 0.99 else 0
#     return (val, val, val)

# Skapa en generator för den inlästa bilden

        # if condition(elem):
        #     new_list.append(generator1(i))
        # else:
        #     new_list.append(generator2(i))
