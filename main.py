import logging

class Cheat:
    def __init__(self):
        self.logger = logging.getLogger("Cheat")

    def connect_to_process(self, pid: int):
        self.logger.info("Connecting to process with PID %s", pid)
        # implementation

    def disconnect_from_process(self):
        self.logger.info("Disconnecting from process")
        # implementation

    def findProcessByName(self, name: str):
        self.logger.info("Searching for process by name %s", name)
        # implementation

    def serve(self):
        self.logger.info("Starting to serve")
        # implementation

def main():
    logging.basicConfig(level=logging.INFO)
    cheat = Cheat()
    process_id = cheat.findProcessByName("csgo.exe")
    cheat.connect_to_process(process_id)
    cheat.serve()

if __name__ == "__main__":
    main()