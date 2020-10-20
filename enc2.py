# SCRAMBLE

import cv2
import numpy as np
import random
from emb import *


def encryption2(p, mesg):
    p = str(p)
    print(p)
    i1 = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    i1 = cv2.resize(i1, (256, 256))
    img = embed(i1, mesg)
    i2 = np.zeros((258, 258), dtype="int")
    i3 = np.zeros((258, 258), dtype="int")
    i4 = np.zeros((258, 258), dtype="int")
    i5 = np.zeros((258, 258), dtype="int")
    k1 = [random.randint(0, 255) for i in range(129)]
    k2 = k1[::-1]
    j = 0
    l = 0
    for i in range(0, 258, 2):
        i2[i] = np.roll(img[i], k1[j])
        i2[i+1] = img[i+1]
        j += 1
    i3 = i2.transpose()
    for i in range(1, 258, 2):
        i4[i-1] = i3[i-1]
        i4[i] = np.roll(i3[i], k2[l])
        l += 1
    i5 = i4.transpose()
    g = "C:\\Users\\Adit\\Desktop\\gui\\ImageEncrypted2.jpg"
    cv2.imwrite(g, i5)
    k1 = str(k1)
    with open("C:\\Users\\Adit\\Desktop\\gui\\key2.txt", "w") as f:
        f.write(k1)
