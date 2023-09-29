import cv2
import numpy as np


def unshuffle_image(image):
    height, width = image.shape[:2]
    unshuffled_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            x = (j + i) % width
            y = (j // width + i) % height
            unshuffled_image[y, x] = image[i, j]

    return unshuffled_image


# Load the image
image = cv2.imread("InFile.png")

# Unshuffle the image
unshuffled_image = unshuffle_image(image)

# Save the unshuffled image
cv2.imwrite("OutFile.png", unshuffled_image)

# Display the unshuffled image
cv2.imshow("Unshuffled Image", unshuffled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
