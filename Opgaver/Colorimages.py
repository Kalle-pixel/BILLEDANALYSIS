#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:39:13 2023

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
im_name = "IMG_8545.JPG"
os.chdir(in_dir)
# Read the image.
# Here the directory and the image name is concatenated
# by "+" to give the full path to the image.
im_org = io.imread(in_dir + im_name)

##print data
print(im_org.shape)
print(im_org.dtype)

##plot image
image_rescaled = rescale(im_org, 0.25, anti_aliasing=True,
                         channel_axis=2)

io.imshow(im_org)
plt.title('ardeche image')
io.show()

im_gray = color.rgb2gray(image_rescaled)
im_byte = img_as_ubyte(im_gray)
io.imshow(im_gray)
plt.title('ardeche image')
io.show()

#%%
image_rescaled = rescale(im_org, 0.25, anti_aliasing=True,
                         channel_axis=2)


image_resized = resize(im_org, (im_org.shape[0] // 8,
                       im_org.shape[1] // 2),
                       anti_aliasing=True)


io.imshow(image_resized)
plt.title('ardeche image')
io.show()