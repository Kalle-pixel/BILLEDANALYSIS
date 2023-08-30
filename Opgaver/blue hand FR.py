#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 17:01:40 2023

@author: kallefalk
"""

from skimage import io, img_as_ubyte, color
import matplotlib.pyplot as plt
import os

# Directory containing data and images
in_dir = "/Users/kallefalk/Desktop/DTU/BILLEDANALYSIS/DTUImageAnalysis-main/exercises/ex1-IntroductionToImageAnalysis/data/"

# X-ray image
im_name = "metacarpals.png"
os.chdir(in_dir)

# Read the image
im_org = io.imread(in_dir + im_name)

# Create a mask for white areas
mask = im_org > 150  # Adjust this threshold as needed

# Convert grayscale images to RGB format
im_rgb = color.gray2rgb(im_org)
im_blue = im_rgb.copy()

# Set blue color where the mask is true
im_blue[mask] = [0, 0, 255]

# Display the result
plt.imshow(im_blue)
plt.title('Processed Image')
plt.show()
