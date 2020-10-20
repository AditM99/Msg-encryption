# SCRAMBLE

import cv2
import numpy as np
from emb import *
def decryption2(p,key):
    img = cv2.imread(p, cv2.IMREAD_GRAYSCALE)
    i2 = np.zeros((258, 258), dtype="int")
    i3 = np.zeros((258, 258), dtype="int")
    i4 = np.zeros((258, 258), dtype="int")
    i5 = np.zeros((258, 258), dtype="int")
    key2=key[::-1]
    k1=[]
    k2=[]
    for i in range(129):
        k1.append(key[i] * -1)
        k2.append(key2[i] * -1)
    i2=img.transpose()
    l=0
    j=0
    for i in range(1,258,2):
        i3[i-1]=i2[i-1]
        i3[i]=np.roll(i2[i],k2[l])
        l+=1
    i4=i3.transpose()
    for i in range(0,258,2):
        i5[i]=np.roll(i4[i],k1[j])
        i5[i+1]=i4[i+1]
        j+=1
    i6,m=eject(i5)
    g = "C:\\Users\\Adit\\Desktop\\gui\\ImageDecrypted2.jpg"
    cv2.imwrite(g, i6)
    with open("C:\\Users\\Adit\\Desktop\\gui\\HiddenMessage.txt","w") as f:
        f.write(m)