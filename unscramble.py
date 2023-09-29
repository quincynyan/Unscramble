# library(imager)
# library(purrr)
# set.seed(2)
# library(seriation)

# unscramble <- function(im.s,axis="x",method="TSP",...)
# {
# 	cols <- imsplit(im.s,axis)
# 	#Compute a distance matrix (using L1 - Manhattan - distance)
# 	#Each entry D_ij compares column i to column j
# 	D <- map(cols,as.vector) %>% do.call(rbind,.) %>% dist(method="manhattan")
# 	out <- seriate(D,method=method,...)
# 	cols[get_order(out)] %>% imappend(axis)
# }

# unscramble(im.s,"y") %>% unscramble("x") %>% plot

# unscrambled_image <- unscramble(im, "x") %>% unscramble("y")
# save.image(unscrambled_image, "OutFile.png")
# plot(unscrambled_image)

import numpy as np
from scipy.spatial.distance import cdist
from scipy.optimize import linear_sum_assignment
from PIL import Image


def unscramble(im: Image.Image, axis: str):
    array = np.asarray(im)

    if axis == "y":
        array = array.swapaxes(0, 1)

    # Compute a distance matrix (using L1 - Manhattan - distance)
    # Each entry D_ij compares column i to column j
    D = cdist(array.reshape(-1, 3), array.reshape(-1, 3), metric="cityblock")
    out = linear_sum_assignment(D)[1]

    if axis == "y":
        out = out.reshape(array.shape[1], array.shape[0])
        out = out.swapaxes(0, 1)
    else:
        out = out.reshape(array.shape[0], array.shape[1])

    return Image.fromarray(array[out])


im = Image.open("InFile.png")
unscrambled_image = unscramble(im, "x")
unscrambled_image = unscramble(unscrambled_image, "y")
unscrambled_image.save("OutFile.png")
