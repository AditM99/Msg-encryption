import cv2
import numpy as np


# i1 = cv2.imread('C:\\Users\\Adit\\Desktop\\sharvil.jpeg',cv2.IMREAD_GRAYSCALE)
# i1 = cv2.resize(i1,(4,4))
# # mesg="klpd group info parth aka mullah , naman aka takla , aryan aka maggu , aryann aka dhirendra , divyansh aka dc , varun aka pussi , yash aka goyu , harsh aka bhatura , varadh aka lala adit aka antiquity 1234567890 qwertyuiopasdfghjklzxcvbnm 9876543210 abcdefklpd group info parth aka mullah , naman aka takla , aryan aka maggu , aryann aka dhirendra , divyansh aka dc , varun aka pussi , yash aka goyu , harsh aka bhatura , varadh aka lala adit aka antiquity 1234567890 qwertyuiopasdfghjklzxcvbnm 9876543210 abcdef"
# # mesg="abcdefgh"
def decryption(img2,key):
    img = img2
    roll=key[0]
    add=key[1]
    i = 0
    for row in img2:
        r=roll[i] * -1
        s=add[i] * -1
        img[i] = [x + s for x in img[i]]
        img[i] = np.roll(row, r)
        i += 1
    return img
# i2=combine(i1,mesg)
# i3,k3=encrypt.encryption(i1)
# i4=decryption(i3,k3)
# # i5,m=separate(i4)
# for r in i1:
#     print(r)
# print("*********")
# for r in i3:
#     print(r)
# print("*********")
# for r in i4:
#     print(r)
# print("*********")
# for r in i4:
#     print(r)
# print("*********")
# for r in i5:
#     print(r)
# print("*********")