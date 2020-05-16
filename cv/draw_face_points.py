import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

cv2.line(img, (0, 0), (511, 511), (0, 255, 0))
cv2.circle(img, (50, 100), 8, (255, 0, 0), 4)

# read face points.
all_points = []
with open("./face_points.txt") as f:
    for l in f:
        points = []
        pts_str = l.split(', ')
        for pt in pts_str:
            xy_str = pt.split(',')
            # print(xy_str)
            # break
            points.append([float(xy_str[0].split('(')[1]), float(xy_str[1].split(')')[0])])
        all_points.append(points)

font = cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
index = 170
frame = 0
while (1):
    img = np.zeros((512, 512, 3), np.uint8)
    for p in all_points[index]:
        pp=(int(p[0]/4), int(p[1]/4))
        # print(pp)
        cv2.circle(img, pp, 1, (255, 0, 0), 4)

    cv2.putText(img, 'frame: ' + str(index), (20, 50), font, 0.5, (0xff, 0xff, 0xff), 1)
    
    frame += 1
    if frame % 2 == 0:
        index = (index + 1) % len(all_points)

    # if index > 180:
    #     index = 170

    cv2.imshow("CV_WiNDOWS", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()