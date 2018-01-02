from scipy.misc import imread,imsave
import matplotlib.pyplot as plt
import numpy as np

img = imread('img.png')

'''
w,h = img.shape[:2]
img[:w,:h,0] = 255

plt.imshow(img)
plt.show()

plt.imshow(img[::2,:,:])
plt.show()

plt.imshow(img[:,:,::-1])
plt.show()
'''
'''
img=imread('img.png',True)
img2 = img//2
imsave('img2.png',img.astype(np.uint8))
hist,bins = np.histogram(img,256,(0,256))
#print(hist)
plt.figure()
plt.imshow(img,cmap='gray')
plt.show()
'''
img=imread('img.png',True)
img *=2
np.clip(img,128,128+255)

imsave('img2.png',img.astype(np.uint8))
hist,bins = np.histogram(img,256,(0,256))
plt.imshow(img,cmap='gray')
plt.figure()
plt.plot(hist)
plt.show()
