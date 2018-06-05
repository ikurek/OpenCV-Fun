import cv2

# A simple image display
def displayImage(name, image):
    cv2.imshow(name, image)
    pass

# Convert to grayscale using OpenCV 3.0
# Convert Color method
def toGrayScale(image):
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_grayscale

# Convert to sepia using manual linear filter
def toSepia(image):
    # Read image width, heigth and colour channels
    i,  j, k = image.shape
    # Copy image to new variable
    image_sepia = image
    # Iterate over every pixel
    for x in range(i):
        for y in range(j):
            # Filter red, green and blue with values that represent colours
            # In range of sepia
            R = image[x, y, 2] * 0.393 + image[x, y, 1] * \
                0.769 + image[x, y, 0] * 0.189
            G = image[x, y, 2] * 0.349 + image[x, y, 1] * \
                0.686 + image[x, y, 0] * 0.168
            B = image[x, y, 2] * 0.272 + image[x, y, 1] * \
                0.534 + image[x, y, 0] * 0.131

            # Check if colours are in range [0, 255]
            if R > 255:
                image_sepia[x, y, 2] = 255
            else:
                image_sepia[x, y, 2] = R
            if G > 255:
                image_sepia[x, y, 1] = 255
            else:
                image_sepia[x, y, 1] = G
            if B > 255:
                image_sepia[x, y, 0] = 255
            else:
                image_sepia[x, y, 0] = B

    # Return converted image
    return image_sepia

# Convert to genative using color subtraction
def toNegative(image):
    imageNegative = (255-image)
    return imageNegative


# Load image
image = cv2.imread('image.jpg')

# Show original
displayImage('Alpacas are cool!', image)
cv2.waitKey(0)

# Show grayscale
print('Converting to grayscale...')
displayImage('Alpacas are cool!', toGrayScale(image))
cv2.waitKey(0)

# Show sepia
print('Converting to sepia...')
displayImage('Alpacas are cool!', toSepia(image))
cv2.waitKey(0)

# Show negative
print('Converting to negative...')
displayImage('Alpacas are cool!', toNegative(image))
cv2.waitKey(0)

# End
cv2.destroyAllWindows()
