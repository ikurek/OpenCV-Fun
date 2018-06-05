import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image
img = cv2.imread('image.jpg', 0)

# Perform canny edge detection
edges = cv2.Canny(img, 275, 200)

# Plot input foto on the left
plt.subplot(121), plt.imshow(img, cmap='gray')
# Add title and disable axis markers
plt.title('Input Alpaca'), plt.xticks([]), plt.yticks([])

# Plot edges image on the right
plt.subplot(122), plt.imshow(edges, cmap='gray')
# Add title and disable axis markers
plt.title('Edgy Alpaca'), plt.xticks([]), plt.yticks([])

# Display finished plot
plt.show()
