import cv2
import numpy as np

def combine(img,msg):
    img2 = np.zeros((6,4), dtype=int)
    msg = list(msg)
    m1 = []
    for i in msg:
        m1.append(ord(i))
    img2[:4, :4] = img
    img2[4] = m1[:4]
    img2[5] = m1[4:8]
    return img2

def separate(img):
    msg=[]
    m1=[]
    img2=img[:4, :4]
    m1[:4]=img[4]
    m1[4:8]=img[5]
    for i in m1:
        msg.append(chr(i))
    msg="".join(msg)
    return img2,msg

