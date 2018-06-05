import sys
import cv2 as cv

# Load the image
src = cv.imread("image.jpg")

while 1:
    # Read image info
    rows, cols, channels = map(int, src.shape)
    # Show image in current state
    cv.imshow('Compressed Alpaca', src)
    # Wait for user input
    k = cv.waitKey(0)

    # End on 'Esc' pressed
    if k == 27:
        break
    # Pyramide up 2 times on w pressed
    elif chr(k) == 'w':
        src = cv.pyrUp(src, dstsize=(2 * cols, 2 * rows))

    # Pyramide down 2 times on s pressed
    elif chr(k) == 's':
        src = cv.pyrDown(src, dstsize=(cols // 2, rows // 2))

cv.destroyAllWindows()
