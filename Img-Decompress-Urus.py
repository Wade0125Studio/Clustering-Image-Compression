# -*- coding: utf-8 -*-

from skimage import io
import numpy as np
import cv2

centers = np.load('Codebook-Urus.npy')

c_image = cv2.imread('Compressed_Urus.png',cv2.IMREAD_GRAYSCALE)

image = np.zeros((c_image.shape[0],c_image.shape[1],3),dtype=np.uint8 )
for i in range(c_image.shape[0]):
    for j in range(c_image.shape[1]):
            image[i,j,:] = centers[c_image[i,j],:]
    
cv2.imwrite('Reconstructed-Urus.png',image)
