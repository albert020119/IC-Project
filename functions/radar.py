import pymem.process
import time
import keyboard
from threading import *
import utils.Offsets as Offsets
import win32gui
import win32api
import win32process
import win32con
import time

class Radar(Thread):
    def run(self, pm, client):
        while True: 
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x74\x15\x8B\x47\x08\x8D\x4F\x08',
                                                    clientModule).start() - 1

            pm.write_uchar(address, 0 if pm.read_uchar(address) != 0 else 2)
            time.sleep(0.001)