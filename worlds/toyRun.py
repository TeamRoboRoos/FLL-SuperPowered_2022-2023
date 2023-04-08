from threading import Thread


class toyRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()
        self.arm.run_time(400, 1000, wait=False)

        # self.drive.moveDist(370, heading=0)

        # self.drive.turnTo(40)
        # self.drive.moveDist(420, heading=40)
        # self.drive.turnTo(0)

        # self.drive.moveDist(230, heading=0)

        # self.drive.moveDist(-220, heading=0)
        # self.drive.spinTo(90)

        # self.drive.moveDist(300, heading=0)
        # self.drive.turnTo(39)
        # self.drive.moveDist(630, heading=39)
        # self.drive.turnTo(0)

        # self.drive.moveDist(120, speed=400, heading=0)
        self.drive.moveDist(260, heading=0)
        self.drive.turnTo(41)
        self.drive.moveDist(630, heading=41)
        self.drive.turnTo(0)

        self.drive.moveDist(100, heading=0)
        self.drive.moveDist(-210, heading=0)
        self.drive.spinTo(90)

        # self.drive.lineFollower(distance=50, mode=1,
        #                         speed=120, kp=0.3, ki=0, kd=0)

        # self.arm.run_angle(-600, 200)

        self.drive.lineFollower(mode=1, speed=140, kp=0.3, ki=0, kd=0)
        self.drive.setHead(90)

        self.drive.moveLight(self.config.Rlight, [0, 10], heading=90)
        self.drive.moveDist(250, speed=900, heading=90)
        self.drive.turnTo(120)

        self.drive.moveDist(90, heading=120)

        self.drive.moveDist(-70)
        self.drive.turnTo(90)

        self.drive.moveDist(100)
        self.drive.turnTo(80)
        self.arm.run_time(-1000, 400)
        # Thread(target=self.arm.run_time,
               # args=[-600, 700]).start()

        self.drive.moveDist(270, 500)
        self.drive.moveDist(-30, 250)
        self.drive.spinTo(180)

        self.drive.moveDist(-120, 1000)

        self.config.state.setState(1)