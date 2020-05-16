import cv2
import numpy as np

img = cv2.imread('./header.png')

img = np.float32(img)

##print img.shape
##print img.size
##print img.dtype

cv2.namedWindow('image')

v1, v2 = 3, 1
dx = v1 * 2
fc = v1 * 12.5
p = 50

dst = img
showOriginal = False

while (1):
    blImage = cv2.bilateralFilter(img, dx, fc, fc)
    img2 = blImage - img + 128

    gaussKrnl = (v2 * 2 - 1, v2 * 2 -1)
    gsImage = cv2.GaussianBlur(img2, gaussKrnl, 0)

    img3 = img + 2 * gsImage - 255;

    dst = (img * (100 - p) + img3 * p) / 100;

    if showOriginal:
        dst = np.uint8(img)
    else:
        dst = np.uint8(dst)
    
    cv2.imshow('image', dst)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        showOriginal = not showOriginal

cv2.destroyAllWindows()

##px = dst[100, 100]
##print px
