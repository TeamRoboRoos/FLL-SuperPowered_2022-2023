from threading import Thread


class run2(Thread):
    def __init__(self, config):
        self.config = config

    def run(self):
        print("Run2")
        self.config.drive.moveDist(100000)
        self.config.state.setState(1)
