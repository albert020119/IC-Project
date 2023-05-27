import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from utils import config                                                                       
from main import Cheat



def build_ui():

    root = tk.Tk()
    root.title("Checkbox Example")
    cheat = Cheat(config.CSGO_PROCESS_NAME)
    window_width = 300
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    root.resizable(False, False)


    background_image = Image.open("hacker.jpg")
    background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)

    # Create a background label and place the image on it
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    root.configure(bg="#383e56")

    options = ["Trigger", "Wall", "Radar", "Bunny", "Anti Flash"]
    check_vars = []
    checkboxes = []  # Store references to the checkboxes

    for index, option in enumerate(options):
        var = tk.IntVar()
        check_vars.append(var)
        checkbox = tk.Checkbutton(root, text=option, variable=var, font=("Arial", 12))
        checkbox.configure(bg="#383e56", fg="white", activebackground="#383e56", selectcolor="#70c1b3")
        checkbox.grid(row=index, column=0, padx=10, pady=5, sticky="w")

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
                    
        except Exception as e: 
            print(e)
        root.after(1000, check_checkbox_status)  

    check_checkbox_status()  

    root.grid_rowconfigure(len(options), weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()


