import logging
from functions import antiflash, bunny, wall, aim, radar
import pymem 

class Cheat:
    TRIGGER_ON = False
    RADAR_ON = False 
    NFLASH_ON = False
    BUNNY_ON = False
    WALL_ON = False  

    def __init__(self, process_name: str):
        self.logger = logging.getLogger("Cheat")
        self.logger.info("Connecting to process  %s", process_name)
        self.process = pymem.Pymem(process_name)

    def disconnect_from_process(self):
        self.logger.info("Disconnecting from process")
        # implementation
        #   
    def start_no_flash(self):
        thread = antiflash.AntiFlash()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)
        
    def start_bunny(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread = bunny.Bunny(self.process, client)
        thread.start()

    def start_wall(self):
        thread = wall.Wall()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)

    def start_trigger(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread = aim.Aim(self.process, client)
        thread.start()

    def start_radar(self):
        thread = radar.Radar()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)

