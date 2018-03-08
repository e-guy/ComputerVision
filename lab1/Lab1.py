'''
    Solution for questions specified in 'Lab1.pdf'
'''

import cv2

# Solution for Question 1

def q1():
    # Load images
    img1 = cv2.imread('DataSamples/1.png',0)
    img2 = cv2.imread('DataSamples/2.png',0)
    
    # Defaultly, the size of the two images are same, otherwide, cropping need to be done.
    img1_tmp = img1.copy()
    img2_tmp = img2.copy()
    
    for r in range(img1_tmp.shape[0]):
        for c in range(img1_tmp.shape[1]/2, img1_tmp.shape[1]):
            img1_tmp[r][c]=0
    
    for r in range(img2_tmp.shape[0]):
        for c in range(img2_tmp.shape[1]/2):
            img2_tmp[r][c]=0
    
    # Combine img1_tmp with img2_tmp
    img12 = img1_tmp+img2_tmp
    
    # Display the image
    cv2.imshow('image1',img1)
    cv2.imshow('image2',img2)
    cv2.imshow('new image',img12)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    q1()
