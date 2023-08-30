#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 08:37:20 2023

@author: kallefalk
"""

from skimage import color, io, measure, img_as_ubyte
from skimage.measure import profile_line
from skimage.transform import rescale, resize
import matplotlib.pyplot as plt
import numpy as np
import pydicom as dicom
import os



# Directory containing data and images
in_dir = "/Users/kallefalk/Desktop/DTU/BILLEDANALYSIS/DTUImageAnalysis-main/exercises/ex1-IntroductionToImageAnalysis/data/"

# X-ray image
im_name = "metacarpals.png"
os.chdir(in_dir)
# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)

print(im_org.shape)
print(im_org.dtype)
io.imshow(im_org)
plt.title('Metacarpal image')
io.show()





io.imshow(im_org, vmin=np.amin(im_org), vmax=np.amax(im_org))
plt.title('Metacarpal image (with gray level scaling)')
io.show()


plt.hist(im_org.ravel(), bins=256)
plt.title('Image histogram')
io.show()

h = plt.hist(im_org.ravel(), bins=256)

bin_no = 100
count = h[0][bin_no]
print(f"There are {count} pixel values in bin {bin_no}")

n=50

for i in range(n-1):
   cov = 1/(n-1)*sum(s1[i]*s2[i])