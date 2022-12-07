from pybricks.ev3devices import ColorSensor

# Wrapper class for colorsensor
# Allows for calibration of lightsensor
class MenuSelector:
    def __init__(self, port, colorMenu):
        self.sensor = ColorSensor(port)
        self.min = 0
        self.max = 100
        self.colorMenu = colorMenu

    def color(self):
        return self.sensor.color()

    def index(self):
        return self.colorMenu.index(self.color())
