import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image                                                                       

def build_ui():

    root = tk.Tk()
    root.title("Checkbox Example")

    # Set window size and position
    window_width = 300
    window_height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))
    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Disable window resizing
    root.resizable(False, False)

    # Load the background image
    background_image = Image.open("hacker.jpg")
    background_image = background_image.resize((window_width, window_height), Image.ANTIALIAS)
    background_image = ImageTk.PhotoImage(background_image)

    # Create a background label and place the image on it
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Configure background color
    root.configure(bg="#383e56")

    options = ["Option 1", "Option 2", "Option 3", "Option 4"]
    check_vars = []

    # Create checkboxes and labels
    for index, option in enumerate(options):
        var = tk.IntVar()
        check_vars.append(var)
        checkbox = tk.Checkbutton(root, text=option, variable=var, font=("Arial", 12))
        checkbox.configure(bg="#383e56", fg="white", activebackground="#383e56", selectcolor="#70c1b3")
        checkbox.grid(row=index, column=0, padx=10, pady=5, sticky="w")
                                                                                        
    # Center the checkboxes and button vertically and horizontally
    root.grid_rowconfigure(len(options), weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
