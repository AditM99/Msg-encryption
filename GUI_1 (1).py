# GUI - Jay

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from enc import *
from enc2 import *
from dec import *
from dec2 import *
import cv2
import numpy as np
import ast

decryptedMessage = ''


def DisplayImageEncrypted1():
    imgEncrypt1 = Image.open(
        'C:\\Users\\Adit\\Desktop\\gui\\ImageEncrypted1.jpg')
    imgEncrypt1 = ImageTk.PhotoImage(imgEncrypt1)
    panel = Label(root, image=imgEncrypt1)
    panel.image = imgEncrypt1
    panel.grid(row=7)


def DisplayImageEncrypted2():
    imgEncrypt2 = Image.open(
        'C:\\Users\\Adit\\Desktop\\gui\\ImageEncrypted2.jpg')
    imgEncrypt2 = ImageTk.PhotoImage(imgEncrypt2)
    panel = Label(root, image=imgEncrypt2)
    panel.image = imgEncrypt2
    panel.grid(row=7)


def GetMessage():
    message = messageText.get
    return message


def encrypt1():
    path = InputDirectory.get("1.0", "end-1c")
    message = messageText.get("1.0", "end-1c")
    print(path, message)
    encryption(path, message)


def encrypt2():
    path = InputDirectory.get("1.0", "end-1c")
    message = messageText.get("1.0", "end-1c")
    encryption2(path, message)


def DisplayImageDecrypted1():
    imgDecrypt1 = Image.open(
        'C:\\Users\\Adit\\Desktop\\gui\\ImageDecrypted1.jpg')
    imgDecrypt1 = ImageTk.PhotoImage(imgDecrypt1)
    panel = Label(root, image=imgDecrypt1)
    panel.image = imgDecrypt1
    panel.grid(row=12)


def DisplayImageDecrypted2():
    imgDecrypt2 = Image.open(
        'C:\\Users\\Adit\\Desktop\\gui\\ImageDecrypted2.jpg')
    imgDecrypt2 = ImageTk.PhotoImage(imgDecrypt2)
    panel = Label(root, image=imgDecrypt2)
    panel.image = imgDecrypt2
    panel.grid(row=12)


def decrypt1():
    pathKey = InputDirectoryKey.get("1.0", "end-1c")
    pathOfEncryptedImg = InputDirectoryEncrypt.get("1.0", "end-1c")

    with open(pathKey, "r") as f:
        keyForDecryption = ast.literal_eval(f.read())

    print(pathKey, pathOfEncryptedImg)
    decryption(pathOfEncryptedImg, keyForDecryption)


def decrypt2():
    pathKey = InputDirectoryKey.get("1.0", "end-1c")
    pathOfEncryptedImg = InputDirectoryEncrypt.get("1.0", "end-1c")

    with open(pathKey, "r") as f:
        keyForDecryption = ast.literal_eval(f.read())

    print(pathKey, pathOfEncryptedImg)
    decryption2(pathOfEncryptedImg, keyForDecryption)


def ReadMessageTxt():
    decryptedMessage = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam hendrerit dictum velit, sed sollicitudin tellus rhoncus vel. Integer sed commodo diam. Suspendisse sed malesuada magna. Integer placerat massa risus, sed convallis erat interdum vel. Ut congue quam mi, eget suscipit sapien placerat ac. Integer euismod ex sagittis, sodales lectus vitae, rutrum erat. Nam auctor lorem vel tristique gravida. Nullam facilisis arcu id turpis eleifend, sit amet ullamcorper nulla mattis. In porttitor finibus nibh nechj."
    label3 = Label(text="The message hidden in the image was: ")
    label3.grid(row=15, column=1)
    label4 = Label(text=decryptedMessage)
    label4.grid(row=15, column=2)


root = Tk()
root.title('IMAGE ENCRYPTION')
root.geometry('800x600')
root.resizable(width=True, height=True)


emptyLabel1 = Label(text="                           ")
emptyLabel1.grid(row=1, column=1)

label1 = Label(text="Enter the image path here: ")
label1.grid(row=2, column=1)
InputDirectory = Text(root, height=1, width=40)
InputDirectory.grid(row=2, column=2)

emptyLabel2 = Label(text="                           ")
emptyLabel2.grid(row=3, column=1)

label2 = Label(text="Enter the message you want to be embedded in the image: ")
label2.grid(row=4, column=1)
messageText = Text(root, height=1, width=20)
messageText.grid(row=4, column=2)

emptyLabel3 = Label(text="                           ")
emptyLabel3.grid(row=5, column=1)

encryptButton1 = Button(root, text='Encrypt Method 1', command=lambda: [
                        encrypt1(), DisplayImageEncrypted1()])
encryptButton1.grid(row=6, column=1)
encryptButton2 = Button(root, text='Encrypt Method 2', command=lambda: [
                        encrypt2(), DisplayImageEncrypted2()])
encryptButton2.grid(row=6, column=2)

emptyLabel4 = Label(text="                           ")
emptyLabel4.grid(row=8, column=1)

label6 = Label(text="Enter the Encrypted image path here: ")
label6.grid(row=9, column=1)
InputDirectoryEncrypt = Text(root, height=1, width=40)
InputDirectoryEncrypt.grid(row=9, column=2)

label5 = Label(text="Enter the key path here: ")
label5.grid(row=10, column=1)
InputDirectoryKey = Text(root, height=1, width=40)
InputDirectoryKey.grid(row=10, column=2)

decryptButton1 = Button(root, text='Decrypt Method 1', command=lambda: [
                        decrypt1(), DisplayImageDecrypted1()])
decryptButton1.grid(row=11, column=1)
decryptButton2 = Button(root, text='Decrypt Method 2', command=lambda: [
                        decrypt2(), DisplayImageDecrypted2()])
decryptButton2.grid(row=11, column=2)

emptyLabel5 = Label(text="                           ")
emptyLabel5.grid(row=13, column=1)

GetHiddenMessage = Button(
    root, text='Get Hidden Message', command=ReadMessageTxt)
GetHiddenMessage.grid(row=14, column=1)

root.mainloop()
