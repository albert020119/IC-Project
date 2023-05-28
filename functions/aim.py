import keyboard
import pymem
import pymem.process
import time
from threading import *
import Offsets as Offsets
from multiprocessing import Process, Event


trigger_key = "n"


class Aim(Thread):
    def __init__(self, pm, client, stop_event):
        super().__init__()
        self.pm = pm
        self.client = client
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            if not keyboard.is_pressed(trigger_key):
                time.sleep(0.1)

            if keyboard.is_pressed(trigger_key):
                player = self.pm.read_int(self.client + Offsets.dwLocalPlayer)
                entity_id = self.pm.read_int(player + Offsets.m_iCrosshairId)
                entity = self.pm.read_int(self.client + Offsets.dwEntityList + (entity_id - 1) * 0x10)

                entity_team = self.pm.read_int(entity + Offsets.m_iTeamNum)
                player_team = self.pm.read_int(player + Offsets.m_iTeamNum)

                if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                    self.pm.write_int(self.client + Offsets.dwForceAttack, 6)

                time.sleep(0.006)