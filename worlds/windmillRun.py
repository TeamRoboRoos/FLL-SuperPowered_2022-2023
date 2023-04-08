from threading import Thread


class windmillRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.flipper = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(315, heading=0) #370
        self.drive.moveDist(-20, heading=0, turn=False)
        self.drive.spinTo(-40)
        self.drive.moveDist(370, heading=-40)
        self.drive.spinTo(45)

        # self.drive.moveDist(580, heading=0)
        # self.drive.moveDist(-90, heading=0, turn=False)
        # self.drive.spinTo(-41)
        # self.drive.moveLight(self.config.Rlight, [0, 10], heading=-41)
        # self.drive.moveDist(130, heading=-41)
        # self.drive.spinTo(45)

        # Push the windmill three times
        # self.drive.moveDist(90)
        # self.wait(300)
        # self.drive.moveDist(-50)
        self.drive.moveDist(115)
        self.wait(150)
        self.drive.moveDist(-40)
        self.drive.moveDist(50)
        self.wait(150)
        self.drive.moveDist(-40)
        self.drive.moveDist(50)
        self.wait(150)
        self.drive.moveDist(-40)
        self.drive.moveDist(50)
        self.wait(150)

        # self.drive.setHead(45)

        self.drive.moveDist(-220, heading=45)
        self.drive.spinTo(-41)

        # In place for the car
        # self.drive.moveDist(293, heading=-45)
        self.drive.moveDist(278, heading=-41)
        # self.flipper.run_angle(800, 450)
        self.flipper.run_time(300, 900)
        # self.flipper.run_angle(-900, 450)
        # Thread(target=self.flipper.run_time, args=[-400, 500]).start()
        self.drive.moveDist(-1100, speed=1000, down=False, turn=False, heading=-48)
        self.flipper.stop()

        self.config.state.setState(1)
