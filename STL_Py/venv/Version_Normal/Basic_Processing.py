# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 03:16:49 2019

@author: Baazigar
"""

import cv2
import numpy as np
import os
import random

dirpath=os.getcwd()

def main():
    L = []
    path ="/Users/irateleaf/PycharmProjects/STL_Py/venv/Images"
    imgpath1 = path + "/Side_4.png"
    val = random.randrange(1, 3)
    imgpath2 = path + "/Side_4+"+str(val)+".png"
    val = random.randrange(3, 5)
    imgpath3 = path + "/Side_4+"+str(val)+".png"
    val = random.randrange(1, 11)
    imgpath4 = path + "/Side_4+"+str(val)+".png"
    val = random.randrange(5, 7)
    imgpath5 = path + "/Side_4+"+str(val)+".png"

    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    img3 = cv2.imread(imgpath3, 1)
    img4 = cv2.imread(imgpath4, 1)
    img5 = cv2.imread(imgpath5, 1)

    img1 = cv2.resize(img1, (512, 512))
    img2 = cv2.resize(img2, (512, 512))
    img3 = cv2.resize(img3, (512, 512))
    img4 = cv2.resize(img4, (512, 512))
    img5 = cv2.resize(img5, (512, 512))

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
    img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
    img5 = cv2.cvtColor(img5, cv2.COLOR_BGR2GRAY)

    img1 = cv2.GaussianBlur(img1, (7, 7), 0)  # removes gaussian noise
    img2 = cv2.GaussianBlur(img2, (7, 7), 0)
    img3 = cv2.GaussianBlur(img3, (7, 7), 0)
    img4 = cv2.GaussianBlur(img4, (7, 7), 0)
    img5 = cv2.GaussianBlur(img5, (7, 7), 0)

    img1 = cv2.medianBlur(img1, 3)
    img2 = cv2.medianBlur(img2, 3)
    img3 = cv2.medianBlur(img3, 3)
    img4 = cv2.medianBlur(img4, 3)
    img5 = cv2.medianBlur(img5, 3)
    # removes salt and pepper noise

    img1 = cv2.Canny(img1, 30, 150, L2gradient=True)  # canny edge detection
    img2 = cv2.Canny(img2, 30, 150, L2gradient=True)
    img3 = cv2.Canny(img3, 30, 150, L2gradient=True)
    img4 = cv2.Canny(img4, 30, 150, L2gradient=True)
    img5 = cv2.Canny(img5, 30, 150, L2gradient=True)

    # trying dialation

    kernel = np.ones((3, 3), np.uint8)
    img1 = cv2.dilate(img1, kernel, iterations=3)
    img2 = cv2.dilate(img2, kernel, iterations=3)
    img3 = cv2.dilate(img3, kernel, iterations=3)
    img4 = cv2.dilate(img4, kernel, iterations=3)
    img5 = cv2.dilate(img5, kernel, iterations=3)

    res1 = cv2.absdiff(img1, img2)
    res2 = cv2.absdiff(img1, img3)
    res3 = cv2.absdiff(img1, img4)
    res4 = cv2.absdiff(img1, img5)
    # --- convert the result to integer type ---
    res1 = res1.astype(np.uint8)
    res2 = res2.astype(np.uint8)
    res3 = res3.astype(np.uint8)
    res4 = res4.astype(np.uint8)

    # --- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(res1) * 100) / res1.size
    m = int(percentage * (10 / 8.304977416992188)) + 11
    L.append(m)
    percentage = (np.count_nonzero(res2) * 100) / res2.size
    n = int(percentage * (10 / 8.304977416992188)) + 11
    L.append(n)
    percentage = (np.count_nonzero(res3) * 100) / res3.size
    o = int(percentage * (10 / 8.304977416992188)) + 11
    L.append(o)
    percentage = (np.count_nonzero(res4) * 100) / res4.size
    p = int(percentage * (10 / 8.304977416992188)) + 11
    L.append(p)

    #print(L)
    return L

if __name__ == "__main__":
    main()