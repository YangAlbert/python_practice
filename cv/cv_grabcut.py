import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
imgSz = (512, 512, 3)
edgeColor = (0, 255, 0)
bgColor = (128, 0, 0)

srcImg = cv2.imread('./header.png')
rectImg = srcImg.copy()

maskImg = np.zeros(srcImg.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

cutImg = np.zeros(srcImg.size, np.uint8)

cutDone = False

def draw_rectangle(e, x, y, flags, param):
    global ix, iy, drawing, rectImg, srcImg, cutImg, bgdModel, fgdModel, cutDone

    if cutDone:
        return

    if e == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif e == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
##            rectImg = np.ones(imgSz, np.uint8)
            rectImg = srcImg.copy()
            cv2.rectangle(rectImg, (ix, iy), (x, y), edgeColor, 2)
    elif e == cv2.EVENT_LBUTTONUP:
        drawing = False
        rect = (ix, iy, x, y)
        cv2.grabCut(srcImg, maskImg, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((maskImg==2) | (maskImg==0), 0, 1).astype('uint8')
        cutImg = srcImg.copy()
        cutImg = cutImg * mask2[:, :, np.newaxis]
        cutDone = True
        

winName = 'grabCut_Demo'
cv2.namedWindow(winName)
cv2.setMouseCallback(winName, draw_rectangle)

while (1):
    if cutDone:
        cv2.imshow(winName, cutImg)
    else:
        cv2.imshow(winName, rectImg)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('c'):
        rectImg = srcImg.copy()
    elif k == ord('r'):
        cutDone = False
        rectImg = srcImg.copy()

cv2.destroyAllWindows()
