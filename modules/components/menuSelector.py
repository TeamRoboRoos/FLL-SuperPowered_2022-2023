from pybricks.ev3devices import ColorSensor
from threading import Thread
from time import sleep

# Wrapper class for colorsensor
# Allows for calibration of lightsensor


class MenuSelector:
    def __init__(self, port, colorMenu, defaultColor, state):
        self.sensor = ColorSensor(port)
        self.min = 0
        self.max = 100
        self.colorMenu = colorMenu
        self.values = [defaultColor] * 100
        self.defaultColor = defaultColor
        self.state = state
        self.on = True

    def update(self):
        while True:
            if self.state.getState() == 1:
                color = self.sensor.color()
                self.values.append(color)
                if len(self.values) > 100:
                    self.values.pop(0)
            sleep(0.002)

    def index(self):
        if self.on:
            try:
                return self.colorMenu.index(max(set(self.values), key=self.values.count))
            except:
                return None
        return None

    def color(self):
        return max(set(self.values), key=self.values.count)

    def toggle(self):
        self.on = not self.on
