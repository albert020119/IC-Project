import pymem.process
import time
from threading import *
import utils.Offsets as Offsets


local_player = Offsets.dwLocalPlayer
flash_offset = Offsets.m_flFlashMaxAlpha

#overrides flashed value of player
#another more elegant solution, replace flashed animation with something blankd :D 

class AntiFlash(Thread):
    def run(self, pm, client):
        while True:
            player = pm.read_int(client + local_player)
            if player:
                flash_value = player + flash_offset
                if flash_value:
                    pm.write_float(flash_value, float(0))
            time.sleep(0.01)



