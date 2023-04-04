import pymem.process
import time
from threading import *
from . import Offsets


local_player = Offsets.dwLocalPlayer
flash_offset = Offsets.m_flFlashMaxAlpha

class AntiFlash(Thread):
    def run(self, pm, client, event):
        while True:
            player = pm.read_int(client + local_player)
            if event.isSet():
                break
            if player:
                flash_value = player + flash_offset
            if flash_value:
                pm.write_float(flash_value, float(0))
            time.sleep(0.01)



