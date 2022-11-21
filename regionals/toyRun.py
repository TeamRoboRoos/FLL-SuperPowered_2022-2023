from threading import Thread


class toyRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(320, heading=0)

        self.drive.turnTo(40)
        self.drive.moveDist(420, heading=40)
        self.drive.turnTo(0)

        self.drive.moveDist(280, heading=0)

        self.drive.moveDist(-220, heading=0)
        self.drive.spinTo(90)

        self.drive.lineFollower(mode=1, speed=120, kp=0.3, ki=0, kd=0)
        self.drive.setHead(90)

        self.drive.moveLight(self.config.Rlight, [0, 10], heading=90)
        self.drive.moveDist(270, heading=90)
        self.drive.turnTo(120)

        self.drive.moveDist(80, heading=120)

        self.drive.moveDist(-100)
        self.drive.turnTo(90)
        self.drive.moveDist(400)
        self.drive.spinTo(180)

        self.drive.moveDist(-150)
        self.drive.turnTo(160)

        self.config.state.setState(1)
