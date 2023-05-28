import logging
from functions import antiflash, bunny, wall, aim, radar
import pymem 
import signal
import threading
from multiprocessing import Process, Event

class Cheat:
    TRIGGER_ON = False
    RADAR_ON = False 
    NFLASH_ON = False
    BUNNY_ON = False
    WALL_ON = False  
    thread_dict={}

    def __init__(self, process_name: str):
        self.logger = logging.getLogger("Cheat")
        self.logger.info("Connecting to process  %s", process_name)
        self.process = pymem.Pymem(process_name)
        self.thread_dict={}
        self.stop_flag = threading.Event()  # Create an event object for stopping the thread

    def disconnect_from_process(self):
        self.logger.info("Disconnecting from process")
        # implementation
        #   

    def terminate_thread(self,string) :
        print(self.thread_dict[string])
        self.thread_dict[string].set()

    def start_no_flash(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        stop_event = Event()
        thread = antiflash.AntiFlash(self.process,client, stop_event)
        self.thread_dict['antiflash']=stop_event
        thread.start()
        
    def start_bunny(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        stop_event = Event()
        thread = bunny.Bunny(self.process, client, stop_event)
        self.thread_dict['bunny']=stop_event
        thread.start()

    def start_wall(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        stop_event = Event()
        thread = wall.Wall(self.process, client, stop_event)
        self.thread_dict['wall']=stop_event
        thread.start()

    def start_trigger(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll").lpBaseOfDll
        stop_event = Event()
        thread = aim.Aim(self.process, client, stop_event)
        self.thread_dict['trigger']=stop_event
        thread.start()

    def start_radar(self):
        client = pymem.process.module_from_name(self.process.process_handle, "client.dll")
        stop_event = Event()
        thread = radar.Radar(self.process, client, stop_event)
        self.thread_dict['radar']=stop_event
        thread.start()

