'''
    This is a Python script try to load and display images by using opencv 
    (Source images can be found under the folder './DataSamples/')
    (Useful tutorials refers to: https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#display-image)
'''

#!/usr/bin/python
import cv2

# Load an color image in grayscale
img1 = cv2.imread('DataSamples/2.png',0) 

# Display the image
cv2.imshow('image1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

