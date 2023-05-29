import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from utils import config 
import customtkinter


root = customtkinter.CTk()
root.geometry("500x170")

txt = "GAME IS RUNNING"
count=0
text=''
label = customtkinter.CTkLabel(master=root, text=txt,fg_color="#454B1B")
label.pack(pady=20)
def slider():
    global count,text 
    if (count>=len("GAME IS RUNNING")):
        count=-1
        text=''
        label.configure(text=text)
    else:
        text = text+ txt[count]
        label.configure(text=text)
    count+=1
    label.after(100,slider)
slider()

root.mainloop()