import cv2
import numpy as np

from tkinter import * 
from PIL import Image, ImageTk 
#Creating Tkinter Window and Label 
root = Tk() 
video = Label(root) 
video.pack() 
vid = cv2.VideoCapture(0) 


#Loop which display video on the label 
while(True):
    ret, frame = vid.read() #Reads the video
    #Converting the video for Tkinter
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    #Setting the image on the label
    video.config(image=imgtk)
    root.update() #Updates the Tkinter window 
vid.release() 
cv2.destroyAllWindows()
