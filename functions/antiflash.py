import pymem.process
import time
from threading import *
import Offsets as Offsets


local_player = Offsets.dwLocalPlayer
flash_offset = Offsets.m_flFlashMaxAlpha

#overrides flashed value of player
#another more elegant solution, replace flashed animation with something blankd :D 

class AntiFlash(Thread):
    def __init__(self,pm,client,stop_event):
        super().__init__()
        self.pm = pm 
        self.client = client
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            player = self.pm.read_int(self.client + local_player)
            if player:
                flash_value = player + flash_offset
                if flash_value:
                    self.pm.write_float(flash_value, float(0))
            time.sleep(0.01)



