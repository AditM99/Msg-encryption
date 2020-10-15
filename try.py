import cv2
import numpy as np
import random
from tp import *
from emb import *

def decrypt(img,key):
    i2 = np.zeros((6, 6), dtype="int")
    i3 = np.zeros((6, 6), dtype="int")
    i4 = np.zeros((6, 6), dtype="int")
    i5 = np.zeros((6, 6), dtype="int")
    key2=key[::-1]
    k1=[]
    k2=[]
    for i in range(3):
        k1.append(key[i] * -1)
        k2.append(key2[i] * -1)
    # print(k1)
    # print(k2)
    i2=img.transpose()
    l=0
    j=0
    for i in range(1,6,2):
        i3[i-1]=i2[i-1]
        i3[i]=np.roll(i2[i],k2[l])
        l+=1
    i4=i3.transpose()
    for i in range(0,6,2):
        i5[i]=np.roll(i4[i],k1[j])
        i5[i+1]=i4[i+1]
        j+=1
    return i5

i1 = cv2.imread('C:\\Users\\Adit\\Desktop\\sharvil.jpeg',cv2.IMREAD_GRAYSCALE)
i1 = cv2.resize(i1,(4,4))
mesg="abcdefgh"
img2=embed(i1,mesg)
img3,ke=encrypt(img2)
img4=decrypt(img3,ke)
img5,me=eject(img4)
for r in i1:
    print(r)
print("*********")
for r in img2:
    print(r)
print("*********")
for r in img3:
    print(r)
print("*********")
for s in img4:
    print(s)
print("*********")
for s in img5:
    print(s)
print(me)
c=i1==img5
print(c.all())




