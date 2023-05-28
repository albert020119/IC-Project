import pymem.process
import time
import keyboard
from threading import *
import utils.Offsets as Offsets
import time
import re

class Radar(Thread):
    def __init__(self,pm,client,stop_event):
        super().__init__()
        self.pm = pm 
        self.client = client
        self.stop_event = stop_event
    def run(self):
        while not self.stop_event.is_set():
            clientModule = self.pm.read_bytes(self.client.lpBaseOfDll, self.client.SizeOfImage)
            address = self.client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                                    clientModule).start() - 1

            self.pm.write_uchar(address, 0 if self.pm.read_uchar(address) != 0 else 2)
            time.sleep(0.001)