import pymem
import pymem.process
from threading import *
from Offsets import *

m_iGlowIndex = 0x10488
dwGlowObjectManager = 87403120

# crazy idea: replace map with a spoofed version that has no walls :D 

class Wall (Thread):
        def run(self,pm,client):
            while True:
                glow_manager = pm.read_int(client + dwGlowObjectManager)
                #print(glow_manager)
                for i in range(1, 32):  # Entities 1-32 are reserved for players.
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)
                        if entity_team_id == 2:  # Terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(255))   # R
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(0))   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)             # Enable glow

                        elif entity_team_id == 3:  # Counter-terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))   # R
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))   # G
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(255))   # B
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(1))  # Alpha
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow
