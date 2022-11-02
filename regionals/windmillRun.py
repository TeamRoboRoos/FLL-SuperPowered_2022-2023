from threading import Thread


class windmillRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.flipper = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead()

        self.drive.moveDist(590, heading=0)  # Hits the TV
        self.drive.moveDist(-80, heading=0, turn=False)
        self.drive.spinTo(-45)
        self.drive.moveLight(self.config.Rlight, [0, 10], heading=-40)
        self.drive.moveDist(140, heading=-40)
        self.drive.spinTo(45)

        # Push the windmill three times
        self.drive.moveDist(80)
        self.wait(500)
        self.drive.moveDist(-50)
        self.wait(800)
        self.drive.moveDist(80)
        self.wait(500)
        self.drive.moveDist(-50)
        self.wait(800)
        self.drive.moveDist(80)
        self.wait(500)
        self.drive.setHead(45)

        self.drive.moveDist(-230, heading=45)
        self.drive.spinTo(-45)

        # In place for the car
        self.drive.moveDist(293, heading=-45)
        self.flipper.run_angle(900, 450)
        self.flipper.stop()
        self.flipper.run_angle(-900, 450)
        self.flipper.stop()

        # Grabs the rechargable battery and goes home
        self.drive.moveDist(-1100, heading=-45)

        self.config.state.setState(1)
