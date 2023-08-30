#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 16:16:43 2023

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

##Manipulate data



##print data
print(im_org.shape)
print(im_org.dtype)
io.imshow(im_org)
plt.title('ardeche image')
io.show()


mask = im_org > 150
io.imshow(mask)
io.show()

maskrgb = color.gray2rgb(mask)
maskimg = img_as_ubyte(maskrgb)

maskimg[1500:1800,2300:2800 , :] = (0,0,255)

io.imshow(maskimg)
io.show()