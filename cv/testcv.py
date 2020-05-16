import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
##    ret, frame = cap.read()

##    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    img = np.zeros((512, 512, 3), np.uint8)

    cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

    cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

    cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.CV_AA)

    cv2.imshow('frame', img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

print 'video capture finished'

cap.release()
cv2.destroyAllWindows()
