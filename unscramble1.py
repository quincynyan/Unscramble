import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment
from PIL import Image


def imsplit(im_s, axis):
    return np.split(im_s, im_s.shape[1] if axis == "x" else im_s.shape[0], axis=1 if axis == "x" else 0)


def map(cols, func):
    return np.array(list(map(func, cols)))


def seriate(D, method):
    return np.arange(D.shape[0])


def get_order(out):
    return out


def imappend(im, axis):
    return np.concatenate(im, axis=1 if axis == "x" else 0)


def unscramble(im_s, axis="x", method="TSP"):
    cols = imsplit(im_s, axis)
    D = cdist(np.array(cols).reshape(len(cols), -1),
              np.array(cols).reshape(len(cols), -1), metric="cityblock")
    row_ind, col_ind = linear_sum_assignment(D)
    out = np.array(cols)[col_ind].squeeze()
    out = out[:, np.newaxis]  # Add an extra dimension to the array
    return np.concatenate(out, axis=1 if axis == "x" else 0)


im_s = np.array(Image.open("InFile.png"))
unscrambled_image = unscramble(im_s, axis="y")
unscrambled_image = unscramble(unscrambled_image, axis="x")
Image.fromarray(unscrambled_image.astype(np.uint8)).save("OutFile.png")
Image.fromarray(unscrambled_image.astype(np.uint8)).show()
