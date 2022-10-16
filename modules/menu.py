from pybricks.media.ev3dev import Font
from pybricks.parameters import Button
from pybricks.tools import StopWatch, wait


class menu:
    index = 0
    page = 0
    refresh_time = 100

    def __init__(self, config, quiet):
        self.ev3 = config.ev3
        if quiet:
            self.ev3.speaker.set_volume(0)
        self.menu = config.menu
        self.pages = config.menu["pages"]
        del config.menu["pages"]
        self.config = config

        font = Font("Terminal", 16, monospace=True)
        self.ev3.screen.set_font(font)

        if self.ev3.battery.voltage() < 8100:
            self.ev3.speaker.beep(1500, 2000)
        else:
            self.ev3.speaker.beep(frequency=1000, duration=100)

    def update(self):
        self.page = self.wrap_index(self.page, self.pages)
        self.index = self.wrap_index(
            self.index, self.menu[self.pages[self.page]][0])
        self.displayMenu(self.index, self.page)

        wait(self.refresh_time)
        self.refresh_time = 100

        button = self.ev3.buttons.pressed()
        if len(button) == 1:
            if Button.CENTER in button:
                self.run(self.menu[self.pages[self.page]]
                         [1][self.index], isRun=self.page == 0)
                self.index += 1
            elif Button.UP in button:
                self.index -= 1
                self.refresh_time = 400
            elif Button.DOWN in button:
                self.index += 1
                self.refresh_time = 400
            elif Button.LEFT in button:
                if self.menu["left"][self.index] != None:
                    self.menu["left"][self.index]()
                else:
                    print("Nothing assigned")
                self.refresh_time = 400
            elif Button.RIGHT in button:
                self.page += 1
                self.index = 0
                self.refresh_time = 400
        elif self.config.runButton != None and self.config.runButton.pressed() == True:
            self.run(self.menu[self.pages[self.page]]
                     [1][self.index], isRun=self.page == 0)
            self.index += 1

    def wrap_index(self, idx, theList):
        if idx < 0 or idx >= len(theList):
            idx = 0
        return idx

    def displayMenu(self, curr_index, pageIdx):
        self.ev3.screen.clear()
        for item in self.menu[self.pages[pageIdx]][0]:
            if self.menu[self.pages[pageIdx]][0].index(item) == curr_index:
                self.ev3.screen.print(">", item)
            else:
                self.ev3.screen.print(" ", item)
        self.ev3.screen.print(
            self.config.name, ":", self.ev3.battery.voltage(), end="")

    def run(self, func, isRun=True):
        self.ev3.speaker.beep(frequency=1000, duration=250)

        if isRun == False:
            return func()

        self.config.state.setState(self.config.state.running)

        func.start()

        # Wait for 2 seconds or until run button is released
        timer = StopWatch()
        while timer.time() < 2000 and (self.config.runButton != None and self.config.runButton.pressed() ==
                                       True) or Button.CENTER in self.ev3.buttons.pressed():
            wait(20)

        # Wait until run finishes or is stopped via run button
        while self.config.state.getState() != 1:
            if (self.config.runButton != None and self.config.runButton.pressed() ==
                    True) or Button.CENTER in self.ev3.buttons.pressed():
                self.config.state.setState(self.config.state.stop)

            wait(200)

        self.config.stop()
        self.ev3.speaker.beep(frequency=1000, duration=250)
        self.config.state.setState(self.config.state.standby)
