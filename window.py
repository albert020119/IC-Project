import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from utils import config                                                                       
from main import Cheat
import customtkinter


def build_ui():

    root = tk.Tk()
    root.title("Checkbox Example")
    cheat = Cheat(config.CSGO_PROCESS_NAME)
    window_width = 400
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

    # Create a background label and place the image on it
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.configure(bg="#383e56")
    def clickedSettingsButton():
        new_window = tk.Toplevel(root)
        new_window.title("Custom Window")
        
        input_label = tk.Label(new_window, text="Enter a value:")
        input_label.pack()

        input_entry = tk.Entry(new_window)
        input_entry.pack()

        def submit_value():
            value = input_entry.get()
            print("Submitted value:", value)

        submit_button = tk.Button(new_window, text="Submit", command=submit_value)
        submit_button.pack()
    
    
    
    options = ["Trigger", "Wall", "Radar", "Bunny", "Anti Flash"]
    check_vars = []
    checkboxes = []  # Store references to the checkboxes

    for index, option in enumerate(options):
        var = tk.IntVar()
        check_vars.append(var)
        """     checkbox = tk.Checkbutton(root, text=option, variable=var, font=("Arial", 12))
        checkbox.configure(bg="#383e56", fg="white", activebackground="#383e56", selectcolor="#70c1b3")
        #checkbox.grid(row=index, column=0, padx=10, pady=5, sticky="w")
        checkbox.pack(padx=10, pady=5, anchor="w")"""
        checkbox = customtkinter.CTkCheckBox(master=root,text=option,variable=var,onvalue=1,offvalue=0)
        checkbox.pack(padx=5,pady=10,anchor='center')
        checkboxes.append(checkbox)  # Add checkbox reference to the list

    def check_checkbox_status():
        try:

            print("jocul e pornit")
    
            for i, var in enumerate(check_vars):
                if var.get() == 1:
                    checkbox_text = checkboxes[i].cget("text")  # Get the text associated with the checkbox
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
                    checkbox_text = checkboxes[i].cget("text")  # Get the text associated with the checkbox
                    #print(checkbox_text)
                    if checkbox_text == "Trigger" and cheat.TRIGGER_ON == True:
                        cheat.TRIGGER_ON = False
                        cheat.terminate_thread('trigger')
                        print(cheat.TRIGGER_ON)
                    if checkbox_text == "Wall" and cheat.WALL_ON == True:
                        cheat.WALL_ON = False
                        cheat.terminate_thread('wall')
                        print(cheat.TRIGGER_ON)
                    if checkbox_text == "Radar" and cheat.RADAR_ON == True:
                        cheat.RADAR_ON = False
                        cheat.terminate_thread('radar')
                        print(cheat.TRIGGER_ON)
                    if checkbox_text == "Bunny" and cheat.BUNNY_ON == True:
                        cheat.BUNNY_ON = False
                        cheat.terminate_thread('bunny')
                        print(cheat.TRIGGER_ON)
                    if checkbox_text == "Anti Flash" and cheat.NFLASH_ON == True:
                        cheat.NFLASH_ON = False
                        cheat.terminate_thread('antiflash')
                        print(cheat.TRIGGER_ON)
                    
        except Exception as e: 
            print(e)
        root.after(1000, check_checkbox_status)  

    check_checkbox_status()  
    add_settings_image = ImageTk.PhotoImage(Image.open("settings.png").resize((30,30), Image.ANTIALIAS))


    settingsButton = customtkinter.CTkButton(master=root,image=add_settings_image,text="Trigger Key",width=100,height=40,compound="left",command=clickedSettingsButton)
    settingsButton.pack(pady=70,padx=10)
    root.grid_rowconfigure(len(options), weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


