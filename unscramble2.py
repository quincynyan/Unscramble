import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment
import cv2


def unscramble(im_s, axis="x", method="TSP"):
    cols = np.split(
        im_s, im_s.shape[1 if axis == "x" else 0], axis=1 if axis == "x" else 0)
    D = cdist(np.array(cols).reshape(len(cols), -1),
              np.array(cols).reshape(len(cols), -1), metric="cityblock")
    row_ind, col_ind = linear_sum_assignment(D)
    out = np.array(cols)[col_ind].squeeze()
    return np.concatenate(out.reshape(out.shape[0], *out.shape[1:]), axis=1 if axis == "x" else 0)


# Replace with the file path to your input image
input_image_path = "InFile.png"

# Replace with the file path for the desired output image
output_image_path = "path_to_output_image.png"

# Load the input image and convert it to a NumPy array
im_s = cv2.imread(input_image_path)

# Unscramble the image
unscrambled_image = unscramble(im_s, axis="y")
unscrambled_image = unscramble(unscrambled_image, axis="x")

# Save the unscrambled image
cv2.imwrite(output_image_path, unscrambled_image)

# Display the unscrambled image (optional)
cv2.imshow("Unscrambled Image", unscrambled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
