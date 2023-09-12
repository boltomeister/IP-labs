import cv2
# This imports the OpenCV library, which is commonly used for computer vision tasks, 
# including working with images and videos.

import matplotlib.pyplot as plt
# This imports the pyplot module from the matplotlib library. 
# Matplotlib is a popular library for data visualization in Python, 
# and pyplot provides a simple interface for creating and interacting with figures and plots.

image_input = cv2.imread("image2.jpg")
# This line reads the image file "image1.jpg" using the cv2.imread() function from the OpenCV library. 
# The result is stored in the variable image_input.


# ========================================================= #
# TASK: Crop the image.

# Define the coordinates for the region to be cropped
x = 200 # starting x-coordinate
y = 200 # starting y-coordinate
width = 400 # width of cropped region
height = 300 # height of cropped region

# Crop the image using array slicing
cropped_image = image_input[y:y+height, x:x+width, :]
# The last argument is for exception of particular color.

# Display cropped image
cv2.imshow('Supra', cropped_image)
cv2.waitKey(-1)
# ========================================================= #

cv2.imshow('window', image_input)
cv2.waitKey(-1)

plt.imshow(image_input)
# This line uses the matplotlib function imshow() to display the image specified by image_input.

plt.show()
# This line actually shows the image on the screen.
# It is necessary to call this function to display the image after using imshow().