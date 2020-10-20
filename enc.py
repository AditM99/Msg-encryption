# PIXEL VALUE MANUPILATION

import cv2
import numpy as np
import random
from comb_sep import *


def encryption(p, mesg):
    p = str(p)
    i1 = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    i1 = cv2.resize(i1, (256, 256))
    img = combine(i1, mesg)
    img2 = np.zeros((258, 256), dtype=int)
    img3 = np.zeros((258, 256), dtype=int)
    for i in range(258):
        key = [random.randint(0, 255) for i in range(258)]

    k = 0
    l = 0
    for row in img:
        img2[k] = np.roll(row, key[k])
        k += 1
    for i in range(258):
        for j in range(256):
            s = key[i]
            img3[i][j] = ((img2[i][j]+s) % 256)

    g = "C:\\Users\\Adit\\Desktop\\gui\\ImageEncrypted1.jpg"
    cv2.imwrite(g, img3)
    k1 = str(key)
    with open("C:\\Users\\Adit\\Desktop\\gui\\key1.txt", "w") as f:
        f.write(k1)
