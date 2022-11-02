from pybricks.ev3devices import ColorSensor

# Wrapper class for colorsensor
# Allows for calibration of lightsensor
class LightSensor:
    def __init__(self, port):
        self.sensor = ColorSensor(port)
        self.min = 0
        self.max = 100

    # Used to set each object's calibration values
    def setCalValues(self, min, max):
        self.min = min
        self.max = max
        #print(self.port, self.min, self.max)

    # Calibrated version of colorsensor reflection()
    def readLight(self):
        raw_value = self.sensor.reflection()
        if raw_value <= self.min:
            return 0
        elif raw_value >= self.max:
            return 100
        output = ((raw_value - self.min) / (self.max - self.min)) * 100
        return round(output)

    def color(self):
        return self.sensor.color()
