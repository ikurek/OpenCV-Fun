import cv2


def printImageInfo(image):
    # Read shape values
    height, width, channels = image.shape
    # Print stuff
    print("Size: {}b".format(image.size))
    print("Width: {}px".format(width))
    print("Height: {}px".format(height))
    print("Channels: {}".format(channels))
    print("Pixels: {}".format(width*height))
    pass


def displayImage(image):
    cv2.imshow('Alpacas are cool!', image)
    pass


# Load image
image = cv2.imread('image.jpg')
# Print image info in terminal
printImageInfo(image)
# Display image
displayImage(image)
# End on input
cv2.waitKey(0)
cv2.destroyAllWindows()
