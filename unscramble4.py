import numpy as np
from PIL import Image


def scramble(im, axis="x"):
    im_array = np.array(im)
    h, w, _ = im_array.shape
    if axis == "x":
        permuted = np.random.permutation(w)
        return np.take(im_array, permuted, axis=1)
    elif axis == "y":
        permuted = np.random.permutation(h)
        return np.take(im_array, permuted, axis=0)


def unscramble(im_s, axis="x"):
    im_array = np.array(im_s)
    h, w, _ = im_array.shape
    if axis == "x":
        order = np.argsort(np.random.random(w))
        return np.take(im_array, order, axis=1)
    elif axis == "y":
        order = np.argsort(np.random.random(h))
        return np.take(im_array, order, axis=0)


# Load the scrambled image
scrambled_image = Image.open('InFile.png')

# Perform unscrambling
im_s = scramble(scrambled_image, axis="x")
im_s = scramble(im_s, axis="y")
unscrambled_image = Image.fromarray(unscramble(im_s, axis="x"))

# Save the unscrambled image
unscrambled_image.save('unscrambled_image.png')
