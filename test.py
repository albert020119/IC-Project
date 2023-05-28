import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from utils import config 
import customtkinter


root = customtkinter.CTk()
root.geometry("500x170")


add_folder_image = ImageTk.PhotoImage(Image.open("settings.png").resize((30,30), Image.ANTIALIAS))


button = customtkinter.CTkButton(master=root,image=add_folder_image,text="Bind",width=100,height=40,compound="left")
button.pack(pady=20,padx=20)

root.mainloop()