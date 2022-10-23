from threading import Thread


class powerPlantRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.LMmotor

    def run(self):
        self.drive.setHead(-90)
        self.drive.moveDist(665, 600, heading=-90)
        self.arm.run_angle(-200, 200)
        self.drive.moveDist(-700, 1000, heading=-95, turn=False, down=False)
        self.arm.stop()

        self.config.state.setState(1)
