from threading import Thread


class solarRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        # self.xlift = config.xlift
        self.wait = config.timer.wait

    def run(self):
        self.config.state.setState(1)
