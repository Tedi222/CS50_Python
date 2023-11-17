import cv2 as cv
import numpy as np
import skimage.io
import skimage.color
import matplotlib.pyplot as plt

example = skimage.io.imread("coins.jpg",)
example = skimage.color.rgb2gray(example)
prewitt_win = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
pad = 5
if pad:
    padded_img = np.ones((example.shape[0] + 2*pad, example.shape[1] + 2*pad))
    padded_img[pad:-pad, pad:-pad] = example
else:
    padded_img = example

plt.figure()
plt.subplot(121)
plt.imshow(example, cmap="gray")
plt.title(f"example image of size: {example.shape}")
plt.subplot(122)
plt.imshow(padded_img[0:50, 0:20], cmap="gray")
plt.title(f"padded image of size: {padded_img.shape}")
plt.show()
# print(padded_img[:,6][0:20].shape)



def filt(img, kernel, pad=1):
    if pad:
        padded_img = np.zeros((img.shape[0] + 2 * pad, img.shape[1] + 2 * pad))
        padded_img[pad:-pad, pad:-pad] = img
    else:
        padded_img = img

    res = np.zeros_like(padded_img)
    imx, imy = img.shape
    mx, my = kernel.shape
    mp = int(np.floor(mx/2))
    for i in range(mp, imx+1-mp):
        for j in range(mp, imy+1-mp):
            res[i, j] = np.sum(kernel * padded_img[i-mp:i+mp+1, j-mp:j+mp+1])

    return res[pad:-pad, pad:-pad]


edgey = filt(img=example, kernel=prewitt_win, pad=1)
plt.figure()
plt.imshow(edgey, cmap="gray")
plt.title(f"prewit Y image of size: {edgey.shape}")
plt.show()

edgex = filt(img=example, kernel=np.transpose(prewitt_win), pad=1)
plt.figure()
plt.imshow(edgex, cmap="gray")
plt.title(f"prewit X image of size: {edgex.shape}")
plt.show()

mag = np.sqrt(edgex**2 + edgey**2)
plt.figure()
plt.imshow(mag, cmap="gray")
plt.title(f"magnitude image of size: {mag.shape}")
plt.show()