import pymem
import pymem.process
from threading import *
from Offsets import *

m_iGlowIndex = 0x10488
dwGlowObjectManager = 87398792

# crazy idea: replace map with a spoofed version that has no walls :D 

class Wall (Thread):
    def __init__(self,pm,client,stop_event):
        super().__init__()
        self.pm = pm 
        self.client = client
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            glow_manager = self.pm.read_int(self.client + dwGlowObjectManager)
            #print(glow_manager)
            for i in range(1, 32):  # Entities 1-32 are reserved for players.
                entity = self.pm.read_int(self.client + dwEntityList + i * 0x10)

                if entity:
                    entity_team_id = self.pm.read_int(entity + m_iTeamNum)
                    entity_glow = self.pm.read_int(entity + m_iGlowIndex)
                    if entity_team_id == 2:  # Terrorist
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(255))   # R
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))   # B
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                        self.pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)             # Enable glow

                    elif entity_team_id == 3:  # Counter-terrorist
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(255))   # B
                        self.pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                        self.pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow
