import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image in black and white mode
image = cv2.imread('image.jpg', 0)


def fourierTransform(image):
    # Perform Fourier transform
    fourierTransformArray = np.fft.fft2(image)
    # Shift zero component to middle of image
    shiftedFourierTransformArray = np.fft.fftshift(fourierTransformArray)
    # Create image from Fourier transform array
    magnitudeSpectrumImage = 20*np.log(np.abs(shiftedFourierTransformArray))
    return magnitudeSpectrumImage


# Plot input foto on the left
plt.subplot(121), plt.imshow(image, cmap='gray')
# Add title and disable axis markers
plt.title('Input Alpaca'), plt.xticks([]), plt.yticks([])

# Plot magnitute image on the right
plt.subplot(122), plt.imshow(fourierTransform(image), cmap='gray')
# Add title and disable axis markers
plt.title('Magnitude Spectrum of Alpaca'), plt.xticks([]), plt.yticks([])

# Display finished plot
plt.show()
