library(imager)
library(purrr)
set.seed(2)
library(seriation)

unscramble <- function(im.s,axis="x",method="TSP",...)
{
	cols <- imsplit(im.s,axis)
	#Compute a distance matrix (using L1 - Manhattan - distance)
	#Each entry D_ij compares column i to column j  
	D <- map(cols,as.vector) %>% do.call(rbind,.) %>% dist(method="manhattan")
	out <- seriate(D,method=method,...)
	cols[get_order(out)] %>% imappend(axis) 
}

unscramble(im.s,"y") %>% unscramble("x") %>% plot

unscrambled_image <- unscramble(im, "x") %>% unscramble("y")
save.image(unscrambled_image, "OutFile.png")
plot(unscrambled_image)
