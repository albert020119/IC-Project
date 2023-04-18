import pymem.process
import time
import keyboard
from threading import *
import utils.Offsets as Offsets
import win32gui
import win32api
import win32process
import win32con
import time


local_player = Offsets.dwLocalPlayer
dwForceJump = Offsets.dwForceJump
m_fFlags = Offsets.m_fFlags

class Bunny(Thread):
    def run(self, pm, client):
        while True:
            fg_win = win32gui.GetForegroundWindow()
            pid = win32process.GetWindowThreadProcessId(fg_win)[1]
            handle = win32api.OpenProcess(0x0400, False, pm.process_id)
            app_name = win32process.GetModuleFileNameEx(handle, 0)
            if not ("csgo" in app_name):
                continue
            if keyboard.is_pressed("space"):
                force_jump = client + dwForceJump
                player = pm.read_int(client + local_player)
                if player:
                    on_ground = pm.read_int(player + m_fFlags)
                    if on_ground and on_ground == 257:
                        pm.write_int(force_jump, 5)
                        time.sleep(0.08)
                        pm.write_int(force_jump, 4)

            time.sleep(0.001)
