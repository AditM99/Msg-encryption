import cv2
import numpy as np
import random
from emb import *

# i1 = cv2.imread('C:\\Users\\Adit\\Desktop\\sharvil.jpeg',cv2.IMREAD_GRAYSCALE)
# i1 = cv2.resize(i1,(4,4))
# mesg="abcdefgh"
def encrypt(img):
    i2=np.zeros((6,6),dtype="int")
    i3=np.zeros((6,6),dtype="int")
    i4=np.zeros((6,6),dtype="int")
    i5=np.zeros((6,6),dtype="int")
    k1=[random.randint(-3,3) for i in range(3)]
    k2=k1[::-1]
    # print(k1)
    # print(k2)
    j=0
    l=0
    for i in range(0,6,2):
        i2[i]=np.roll(img[i],k1[j])
        i2[i+1]=img[i+1]
        j+=1
    i3=i2.transpose()
    for i in range(1,6,2):
        i4[i-1]=i3[i-1]
        i4[i]=np.roll(i3[i],k2[l])
        l+=1
    i5=i4.transpose()
    return i5,k1
# img2=embed(i1,mesg)
# img3,ke=encrypt(img2)
# for i in i1:
#     print(i)
# print("**************")
# print(ke)
# for i in img2:
#     print(i)
# print("*********")
# for i in img3:
#     print(i)
 #    for s in i2:
 #        print(s)
 #
 #    print("**********")
 #    for t in i3:
 #        print(t)
 #
 #    print("**********")
 #    for u in i6:
 #        print(u)
 #
 #    print("**********")
 #    for v in i5:
 #        print(v)
