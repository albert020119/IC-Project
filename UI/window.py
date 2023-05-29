import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from utils import config                                                                       
from main import Cheat
import customtkinter
from pymem import Pymem, process, exception

cheat = None  
txt = ""
text=''
count=0
label=None
def build_ui():
    global label
    root = tk.Tk()
    root.title("Checkbox Example")
    window_width = 330
    window_height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    root.resizable(False, False)

    
    background_image = Image.open("backgroundWindow.jpg")
    background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)

    lastClickX = 0
    lastClickY = 0
    
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def displayBind(event,label):
        label.config(text=event.keysym,font=("Arial", 25))
        config.key = event.keysym 
        print(config.key)
    root.configure(bg="#383e56")
    def clickedSettingsButton():
        new_window = tk.Toplevel(root)
        new_window.geometry("300x200+300+200")
        new_window.title("Bind Window")
        new_window.configure(bg="black")
        new_window.resizable(False, False)  # Disable window resizing

        frame = tk.Frame(new_window, bg="black")
        frame.pack(pady=20)

        input_label = tk.Label(frame, text="PRESS A KEY", font=("Arial", 25), pady=10,bg="black",fg="white")
        input_label.pack()

        new_window.bind("<KeyPress>", lambda event: displayBind(event, input_label))
        
        
        submit_button = customtkinter.CTkButton(frame, text="Confirm", command=new_window.destroy,fg_color="white",text_color="black",corner_radius=5)
        submit_button.pack(pady=10)



        # Center the window on the screen
        new_window.update_idletasks()
        width = new_window.winfo_width()
        height = new_window.winfo_height()
        x = (new_window.winfo_screenwidth() // 2) - (width // 2)
        y = (new_window.winfo_screenheight() // 2) - (height // 2)
        new_window.geometry(f"{width}x{height}+{x}+{y}")

        new_window.focus()  # Set focus to the new window

        root.wait_window(new_window)  # Wait until the new window is closed

  
    
    options = ["Trigger", "Wall", "Radar", "Bunny", "Anti Flash"]
    check_vars = []
    checkboxes = [] 
    def slider(label,txt):
        global count,text 
        if (count>=len(txt)):
            count=-1
            text=''
            label.configure(text=text)
        else:
            text = text+ txt[count]
            label.configure(text=text)
        count+=1
        label.after(150,slider,label,txt)

    label = Label(root,text='PROCESS DETACHED',bg="#FF0000")
    label.pack(pady=20)
    def clickedAttachButton():
        global cheat  

        if cheat is None:
            cheat = Cheat(config.CSGO_PROCESS_NAME)
            txt="PROCESS IS ATTACHED"
            label.configure(text=txt,bg="#454B1B")

        else:
            print("Cheat is already attached")
    
    def clickedDetachButton():
        global cheat  

        if cheat is not None:
            cheat.terminate_allThreads()
            cheat = None
            txt="PROCESS DETACHED"
            label.configure(text=txt,bg="#FF0000")

        else:
            print("Cheat is already detached")

    for index, option in enumerate(options):
        var = tk.IntVar()
        check_vars.append(var)
        """     checkbox = tk.Checkbutton(root, text=option, variable=var, font=("Arial", 12))
        checkbox.configure(bg="#383e56", fg="white", activebackground="#383e56", selectcolor="#70c1b3")
        #checkbox.grid(row=index, column=0, padx=10, pady=5, sticky="w")
        checkbox.pack(padx=10, pady=5, anchor="w")"""
        checkbox = customtkinter.CTkCheckBox(master=root,text=option,variable=var,onvalue=1,offvalue=0)
        checkbox.pack(padx=5,pady=10,anchor='n')
        checkboxes.append(checkbox)  

    def check_checkbox_status():
        try:          
            for i, var in enumerate(check_vars):
                if var.get() == 1:
                    checkbox_text = checkboxes[i].cget("text")
                    if checkbox_text == "Trigger" and not cheat.TRIGGER_ON:
                        cheat.TRIGGER_ON = True
                        cheat.start_trigger()
                        print(cheat.TRIGGER_ON)
                    if checkbox_text == "Wall" and not cheat.WALL_ON:
                        cheat.WALL_ON = True
                        cheat.start_wall()
                    if checkbox_text == "Radar" and not cheat.RADAR_ON:
                        cheat.RADAR_ON = True
                        cheat.start_radar()
                    if checkbox_text == "Bunny" and not cheat.BUNNY_ON:
                        cheat.BUNNY_ON = True
                        cheat.start_bunny()   
                    if checkbox_text == "Anti Flash" and not cheat.NFLASH_ON:
                        cheat.NFLASH_ON = True
                        cheat.start_no_flash()      
                elif var.get()==0:
                    checkbox_text = checkboxes[i].cget("text")
                    if checkbox_text == "Trigger" and cheat.TRIGGER_ON == True:
                        cheat.TRIGGER_ON = False
                        cheat.terminate_thread('trigger')
                    if checkbox_text == "Wall" and cheat.WALL_ON == True:
                        cheat.WALL_ON = False
                        cheat.terminate_thread('wall')
                    if checkbox_text == "Radar" and cheat.RADAR_ON == True:
                        cheat.RADAR_ON = False
                        cheat.terminate_thread('radar')
                    if checkbox_text == "Bunny" and cheat.BUNNY_ON == True:
                        cheat.BUNNY_ON = False
                        cheat.terminate_thread('bunny')
                    if checkbox_text == "Anti Flash" and cheat.NFLASH_ON == True:
                        cheat.NFLASH_ON = False
                        cheat.terminate_thread('antiflash')
                    
        except Exception as e: 
            print("e")

        root.after(1000, check_checkbox_status)  


    check_checkbox_status()  
    
    add_settings_image = ImageTk.PhotoImage(Image.open("settings.png").resize((30,30), Image.ANTIALIAS))
    add_attach_image = ImageTk.PhotoImage(Image.open("claw.png").resize((30,30), Image.ANTIALIAS))
    add_disconnect_image = ImageTk.PhotoImage(Image.open("disconnect.png").resize((30,30), Image.ANTIALIAS))

    settingsButton = customtkinter.CTkButton(master=root,image=add_settings_image,text="Trigger Key",corner_radius=15,width=100,height=40,compound="left",command=clickedSettingsButton)
    settingsButton.pack(pady=10,padx=10)
    attachButton = customtkinter.CTkButton(master=root,image=add_attach_image,text="ATTACH",corner_radius=15,width=100,height=40,compound="left",command=clickedAttachButton)
    attachButton.pack(pady=10,padx=10)  
    disconnectButton = customtkinter.CTkButton(master=root,image=add_disconnect_image,text="DETACH",corner_radius=15,width=100,height=40,compound="left",command=clickedDetachButton)
    disconnectButton.pack(pady=10,padx=10)



    
    root.grid_rowconfigure(len(options), weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


