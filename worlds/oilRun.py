from threading import Thread


class oilRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(220)
        self.drive.moveDist(-400, down=False)

        self.config.state.setState(1)
