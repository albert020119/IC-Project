import logging
import pymem
from functions import antiflash, bunny, wall, aim

CSGO_PROCESS_NAME = "csgo.exe"

class Cheat:
    def __init__(self):
        self.logger = logging.getLogger("Cheat")

    def connect_to_process(self, process_name: str):
        self.logger.info("Connecting to process  %s", process_name)
        self.process = pymem.Pymem(process_name)
        # implementation

    def disconnect_from_process(self):
        self.logger.info("Disconnecting from process")
        # implementation

    def serve(self):
        self.logger.info("Starting to serve")
        # implementation
    
    def start_no_flash(self):
        thread = antiflash.AntiFlash()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)
        
    def start_bunny(self):
        thread = bunny.Bunny()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)

    def start_wall(self):
        thread = wall.Wall()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)

    def start_aim(self):
        thread = aim.Aim()
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        thread.run(self.process, client)

def main():
    cheat = Cheat()
    cheat.connect_to_process(CSGO_PROCESS_NAME)
    cheat.start_aim()
    

if __name__ == "__main__":
    main()