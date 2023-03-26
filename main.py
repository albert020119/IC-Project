import logging
import pymem
from tkinter import *

CSGO_PROCESS_NAME = "csgo.exe"

class Cheat:
    def __init__(self):
        self.logger = logging.getLogger("Cheat")

    def connect_to_process(self, process_name: str):
        self.logger.info("Connecting to process  %s", process_name)
        self.process = pymem.Pymem(process_name)
        # implementation

    def disconnect_from_process(self):
        self.logger.info("Disconnecting from process")
        # implementation

    def serve(self):
        self.logger.info("Starting to serve")
        # implementation

def build_window():
    window = Tk()

    window.title("Cheat boss")
    window.configure(width=500, height=300)
    window.configure(bg='lightgray')
    window.geometry("500x500")
    l = Label(window, text = "CSGO cheat")
    l.config(font =("Courier", 14))
    l.pack()

    button1_state = BooleanVar()
    button2_state = BooleanVar()
    button3_state = BooleanVar()

    button1 = Checkbutton(window, text="ESP", variable=button1_state)
    button2 = Checkbutton(window, text="Aim bot", variable=button2_state)
    button3 = Checkbutton(window, text="Trigger bot", variable=button3_state)

    # Add the buttons to the window
    button1.pack()
    button2.pack()
    button3.pack()

    window.mainloop()


def main():
    build_window()
    cheat = Cheat()
    cheat.connect_to_process(CSGO_PROCESS_NAME)
    

if __name__ == "__main__":
    main()