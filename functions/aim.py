import keyboard
import pymem
import pymem.process
import time
from win32gui import GetWindowText, GetForegroundWindow
from threading import *
import utils.Offsets as Offsets


trigger_key = "n"


class Aim(Thread):
    def run(self,pm,client):
        while True:
            if not keyboard.is_pressed(trigger_key):
                time.sleep(0.1)


            if keyboard.is_pressed(trigger_key):
                print("pressed")
                player = pm.read_int(client + Offsets.dwLocalPlayer)
                entity_id = pm.read_int(player + Offsets.m_iCrosshairId)
                entity = pm.read_int(client + Offsets.dwEntityList + (entity_id - 1) * 0x10)

                entity_team = pm.read_int(entity + Offsets.m_iTeamNum)
                player_team = pm.read_int(player + Offsets.m_iTeamNum)

                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    pm.write_int(client + Offsets.dwForceAttack, 6)

                time.sleep(0.006)