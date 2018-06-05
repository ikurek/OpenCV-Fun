import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image.jpg')
colors = ('B', 'G', 'R')

for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])


plt.xlabel('Color values ( range [0, 255] )')
plt.ylabel('Pixels with colour')
plt.show()