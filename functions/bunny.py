import pymem.process
import time
import keyboard
from threading import *
from functions.Offsets import Offsets 
import win32gui
import win32process
import win32api
import time


local_player = Offsets.dwLocalPlayer
dwForceJump = Offsets.dwForceJump
m_fFlags = Offsets.m_fFlags

class Bunny(Thread):
    def __init__(self,pm,client,stop_event):
        super().__init__()
        self.pm = pm 
        self.client = client
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            fg_win = win32gui.GetForegroundWindow()
            pid = win32process.GetWindowThreadProcessId(fg_win)[1]
            handle = win32api.OpenProcess(0x0400, False, self.pm.process_id)
            app_name = win32process.GetModuleFileNameEx(handle, 0)
            if not ("csgo" in app_name):
                continue
            if keyboard.is_pressed("space"):
                force_jump = self.client + dwForceJump
                player = self.pm.read_int(self.client + local_player)
                if player:
                    on_ground = self.pm.read_int(player + m_fFlags)
                    if on_ground and on_ground == 257:
                        self.pm.write_int(force_jump, 5)
                        time.sleep(0.08)
                        self.pm.write_int(force_jump, 4)

            time.sleep(0.001)
