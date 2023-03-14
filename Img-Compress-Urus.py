# -*- coding: utf-8 -*-

from skimage import io
import cv2
from sklearn.cluster import KMeans
import numpy as np



image=cv2.imread('Original-Urus.png')

# cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
# cv2.imshow('My Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


rows = image.shape[0]
cols = image.shape[1]
 
image = image.reshape(image.shape[0]*image.shape[1],3)
kmeans = KMeans(n_clusters = 128, n_init=10, max_iter=200)
kmeans.fit(image)

clusters = np.asarray(kmeans.cluster_centers_,dtype=np.uint8) 
labels = np.asarray(kmeans.labels_,dtype=np.uint8 )  
labels = labels.reshape(rows,cols); 

np.save('Codebook-Urus.npy',clusters)    
cv2.imwrite('Compressed_Urus.png',labels)



