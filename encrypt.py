import cv2
import numpy as np
import random
from comb_sep import *

def encryption(img):
    # for i in img:
    #     print(i)
    # print("*********")
    img2=np.zeros((6,4),dtype=int)
    roll = []
    add = []
    key = []
    k=0
    for row in img:
        r=random.randint(-2,2)
        s=random.randint(-2,2)
        roll.append(r)
        add.append(s)
        img2[k]=np.roll(row,r)
        img2[k]=[x+s for x in img2[k]]
        k+=1
    key.append(roll)
    key.append(add)
    # for i in img2:
    #     print(i)
    # print("********")
    return img2,key

# def decryption(img2,key):
#     img = img2
#     roll=key[0]
#     add=key[1]
#     i = 0
#     for row in img2:
#         r=roll[i] * -1
#         s=add[i] * -1
#         img[i] = [x + s for x in img[i]]
#         img[i] = np.roll(row, r)
#         i += 1
#     return img

i1 = cv2.imread('C:\\Users\\Adit\\Desktop\\sharvil.jpeg',cv2.IMREAD_GRAYSCALE)
i1 = cv2.resize(i1,(4,4))
mesg="abcdefgh"
i2=combine(i1,mesg)
i3,ke=encryption(i2)
# i4=decryption(i3,ke)
# i5,me=separate(i4)
print(ke)
# print(me)
for i in i1:
    print(i)
print("**********")
for i in i2:
    print(i)
print("******")
for i in i3:
    print(i)
print("******")
# for z in i4:
#     print(z)
# print("******")
# for i in i5:
#     print(i)
# print("******")







