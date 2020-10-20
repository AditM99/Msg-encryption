#PIXEL VALUE MANUPILATION - Naman

import cv2
import numpy as np
import ast
from comb_sep import *

def decryption(p,key):
    img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    k1=[]
    img2 = np.zeros((258, 256), dtype=int)
    img3 = np.zeros((258, 256), dtype=int)
    for i in range(258):
        k1.append(key[i] * -1)
    k=0
    for row in img:
        img2[k] = np.roll(row,k1[k])
        k += 1
    for i in range(258):
        for j in range(256):
            s=k1[i]
            s1=img2[i][j]+s
            if(s1<=0):
                s1+=255
            img3[i][j]=s1

    i6,m=separate(img3)
    g = "C:\\Users\\Adit\\Desktop\\gui\\ImageDecrypted1.jpg"
    cv2.imwrite(g, i6)
    with open("C:\\Users\\Adit\\Desktop\\gui\\HiddenMessage.txt","w") as f:
        f.write(m)