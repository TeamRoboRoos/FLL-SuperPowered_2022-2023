from threading import Thread


class powerPlantRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.LMmotor

    def run(self):
        self.drive.setHead(-90)
        self.drive.moveDist(640, 1000, heading=-93)
        self.arm.run_angle(-1000, 300)
        self.drive.moveDist(50, heading=-93)
        Thread(target=self.arm.run_angle, args=[1000, 300]).start()
        self.drive.moveDist(-700, 1000, heading=-93, turn=False, down=False)
        self.arm.stop()
        
        self.config.state.setState(1)
