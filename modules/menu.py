class menu:
    index = 0
    page = 0
    refresh = 100

    def __init__(self, ev3, menu, runButton=None):
        self.ev3 = ev3
        self.menu = menu

        if ev3.battery.voltage() < 8100:
            ev3.speaker.beep(1500, 2000)
        else:
            ev3.speaker.beep(frequency=1000, duration=100)

    def update(self):
        pass
