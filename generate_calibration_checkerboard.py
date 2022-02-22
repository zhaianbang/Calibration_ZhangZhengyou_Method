import cv2
import numpy as np

cube = 90
row_corner = 9
col_corner = 12
img = np.zeros((row_corner * cube, col_corner * cube, 1), dtype="uint8")
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i, j] = 255
        if (int(i / cube) % 2 == 0) and (int(j / cube) % 2 == 0):
            img[i, j] = 0
        if (int(i / cube) % 2 == 1) and (int(j / cube) % 2 == 1):
            img[i, j] = 0

cv2.imwrite("board.jpg", img)
