from threading import Thread


class toyRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()
        self.arm.run_time(200, 1000, wait=False)

        self.drive.moveDist(370, heading=0)

        self.drive.turnTo(40)
        self.drive.moveDist(420, heading=40)
        self.drive.turnTo(0)

        self.drive.moveDist(230, heading=0)

        self.drive.moveDist(-220, heading=0)
        self.drive.spinTo(90)

        # self.drive.lineFollower(distance=50, mode=1,
        #                         speed=120, kp=0.3, ki=0, kd=0)

        # self.arm.run_angle(-600, 200)

        self.drive.lineFollower(mode=1, speed=120, kp=0.3, ki=0, kd=0)
        self.drive.setHead(90)

        self.drive.moveLight(self.config.Rlight, [0, 10], heading=90)
        self.drive.moveDist(270, heading=90)
        self.drive.turnTo(120)

        self.drive.moveDist(80, heading=120)

        self.drive.moveDist(-60)
        self.drive.turnTo(90)

        self.drive.moveDist(90)
        self.arm.run_time(-600, 500)

        self.drive.moveDist(410)
        self.drive.spinTo(150)

        self.drive.moveDist(-200)

        self.config.state.setState(1)
