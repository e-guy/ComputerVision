'''
    Solution for questions specified in 'Lab1.pdf'
'''

import cv2
import numpy as np

# Solution for Question 1

def q1():
    # Load images
    img1 = cv2.imread('DataSamples/1.png',0)
    img2 = cv2.imread('DataSamples/2.png',0)
    
    # The size of two images are same, defaultly
    img1_tmp = img1.copy()
    img2_tmp = img2.copy()
    
    for r in range(img1_tmp.shape[0]):
        for c in range(img1_tmp.shape[1]/2, img1_tmp.shape[1]):
            img1_tmp[r][c]=0
    
    for r in range(img2_tmp.shape[0]):
        for c in range(img2_tmp.shape[1]/2):
            img2_tmp[r][c]=0
    
    # Combine img1_tmp with img2_tmp 
    img12 = img1_tmp + img2_tmp
    
    # Display the image
    cv2.imshow('image1',img1)
    cv2.imshow('image2',img2)
    cv2.imshow('new image',img12)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def q2():
    '''
    256-gray scale to s-gray scale transformation
    pixel value of s-gray scale: u = v//(256/s)
    pixel value of displaying colour map: v = u*(255/(s-1))
    '''
    # Load images
    img = cv2.imread('DataSamples/3.png',0)
    '''
    # this is for test
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            img[r][c] = c//2
    '''
    scale = 256
    #
    img_32 = img.copy()
    print(img_32)
    for r in range(img_32.shape[0]):
        for c in range(img_32.shape[1]):
            img_32[r][c] = img_32[r][c]//(256/32)*(255/31)
    print(img_32)
    #
    img_8 = img.copy()
    print(img_8)
    for r in range(img_8.shape[0]):
        for c in range(img_8.shape[1]):
            img_8[r][c] = img_8[r][c]//(256/8)*(255/7)
    print(img_8)
    #
    img_2 = img.copy()
    print(img_2)
    for r in range(img_2.shape[0]):
        for c in range(img_2.shape[1]):
            img_2[r][c] = img_2[r][c]//(256/2)*(255/1)
    print(img_2)

    #
    cv2.imshow('256-grey image',img)
    cv2.imshow('32-grey image',img_32)
    cv2.imshow('8-grey image',img_8)
    cv2.imshow('2-grey image',img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    q2()
