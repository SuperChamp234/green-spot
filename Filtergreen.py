import cv2
import imutils
import matplotlib.pyplot as plt
import numpy as np
import os

def slice_image(im, a):
    M = im.shape[0]//a
    N = im.shape[1]//a
    tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]

    i=0
    for tile in tiles:
        cv2.imwrite("tiles/tile" + str(i) + ".jpg", tile)
        i += 1

def import_slices():
    path="tiles/"
    slices = []
    for filename in os.listdir(path):
        if filename.startswith("tile"):
            slices.append(cv2.imread(path + filename))
    return slices

def green_mask(slices,sensitivity=50):
    greens = []
    for slicee in slices:
        hsv = cv2.cvtColor(slicee, cv2.COLOR_BGR2HSV)
        lower_green = np.uint8([60-sensitivity,100,50])
        upper_green = np.uint8([60+sensitivity,255,255])
        mask = cv2.inRange(hsv,lower_green,upper_green)
        imask = mask>0
        green = np.zeros_like(slicee, np.uint8)
        green[imask] = slicee[imask]
        greens.append(green)
    return greens
def save_greens(greens):
    i = 0
    for green in greens:
        cv2.imwrite("green_files/green" + str(i) + ".jpg", green)
        i += 1

#main function
def main():
    im = cv2.imread("testsave.tif")
    slice_image(im, 10)
    slices = import_slices()
    greens = green_mask(slices)
    save_greens(greens)

if __name__ == "__main__":
    main()