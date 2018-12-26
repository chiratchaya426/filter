import cv2
import numpy as np
from matplotlib import pyplot as plt
#import image
img = cv2.imread('cat-png.png')

#boxfilter, avaraging--blur
blur1 = cv2.blur(img,(3,3))
blur2 = cv2.blur(img,(5,5))
blur3 = cv2.blur(img,(7,7))


plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blur1),plt.title('Blurred with 3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(blur2),plt.title('Blurred with 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(blur3),plt.title('Blurred with 7*7')
plt.xticks([]), plt.yticks([])
plt.show()


#Gaussian filter
gs1 = cv2.GaussianBlur(img,(3,3),0)
gs2 = cv2.GaussianBlur(img,(5,5),0)
gs3 = cv2.GaussianBlur(img,(7,7),0)

plt.subplot(221),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(gs1),plt.title('Gaussian with 3*3')
plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(gs2),plt.title('Gaussian with 5*5')
plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(gs3),plt.title('Gaussian with 7*7')
plt.xticks([]), plt.yticks([])
plt.show()
