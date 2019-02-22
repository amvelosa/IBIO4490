# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 21:47:00 2019

@author: NataliaDurán
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage as ndi
import cv2

#Show the image with plt and mpimg
imgo1=mpimg.imread('P2.jpeg')
plt.axis("off")
plt.imshow(imgo1)
plt.show()

#Show the image with cv2 and plt
imgo2=cv2.imread('P1.jpeg')
plt.axis("off")
plt.imshow(cv2.cvtColor(imgo2, cv2.COLOR_BGR2RGB))
plt.show()

#Apply of high-filter with kernel
img1=cv2.imread('P1.jpeg',0)
data = np.array(img1, dtype=float)
kernel = np.array([[-1, -1, -1],
                   [-1,  30, -1],
                   [-1, -1, -1]])
kernel=1/30*kernel
img1= ndi.convolve(data, kernel)
img1 = img1.astype(np.uint8)
img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2RGB)
plt.imshow(img1)
plt.show()

#Apply of low filter (Gaussian)
img2=cv2.imread('P2.jpeg')
d=270
img2 = cv2.GaussianBlur(img2,(27,27),d)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.show()

#Make the hybrid image
img=cv2.addWeighted(img1,0.5,img2,0.5,0)
#Show the image
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

#Try to see the image more little
#imgp=cv2.pyrDown(img)
#imgp=cv2.pyrDown(imgp)
#imgp=cv2.pyrDown(imgp)
#fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5), dpi=80, sharex=True, sharey=True)
#ax[1].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
#ax[0].imshow(cv2.cvtColor(imgp, cv2.COLOR_BGR2RGB))
