from pybricks.parameters import Button
from pybricks.tools import StopWatch, wait
from threading import Thread


class menu:
    index = 0
    page = 0
    refresh = 100

    def __init__(self, config):
        self.ev3 = config.ev3
        self.menu = config.menu
        self.pages = config.menu.keys()
        self.state = config.state.state
        self.config = config

        if self.ev3.battery.voltage() < 8100:
            self.ev3.speaker.beep(1500, 2000)
        else:
            self.ev3.speaker.beep(frequency=1000, duration=100)

    def update(self):
        pageIdx = self.wrap_index(pageIdx, self.pages)
        index = self.wrap_index(index, self.menu[self.pages[pageIdx]][0])
        self.displayMenu(index, pageIdx)

        wait(refresh_time)
        refresh_time = 100

        button = self.ev3.buttons.pressed()
        if len(button) == 1:
            if Button.CENTER in button:
                self.Run(self.menu[self.page[pageIdx]]
                         [1][index], use_dec=pageIdx == 0)
                index += 1
            elif Button.UP in button:
                index -= 1
                refresh_time = 400
            elif Button.DOWN in button:
                index += 1
                refresh_time = 400
            elif Button.LEFT in button:
                if self.config.leftButton != None:
                    self.config.leftButton()
            elif Button.RIGHT in button:
                pageIdx += 1
                index = 0
                refresh_time = 400
        elif self.runButton == None and self.runButton.pressed() == True:
            self.Run(self.menu[self.pages[pageIdx]]
                     [1][index].run, pageIdx == 0)
            index += 1

    def wrap_index(self, idx, theList):
        if idx < 0 or idx >= len(theList):
            idx = 0
        return idx

    def displayMenu(self, curr_index, pageIdx):
        self.ev3.screen.clear()
        for item in self.pages[pageIdx]:
            if self.menu[self.pages[pageIdx]].index(item) == curr_index:
                self.ev3.screen.print(">>>", item)
            else:
                self.ev3.screen.print("   ", item)
        self.ev3.screen.print(
            self.config.name, ":", self.ev3.battery.voltage(), end="")

    def run(self, func, isRun=True):
        self.ev3.speaker.beep(frequency=1000, duration=250)

        if isRun == False:
            return func()

        self.state = self.config.state.running

        Thread(func).start()

        # Wait for 2 seconds or until run button is released
        timer = StopWatch()
        while timer.time() < 2000 and (self.runButton == None and self.runButton.pressed() ==
                                       True) or Button.CENTER in self.ev3.buttons.pressed():
            wait(20)

        # Wait until run finishes or is stopped via run button
        while self.state != self.config.state.standby:
            if (self.runButton == None and self.runButton.pressed() ==
                    True) or Button.CENTER in self.ev3.buttons.pressed():
                self.state = self.config.state.stop

            wait(200)
        self.ev3.speaker.beep(frequency=1000, duration=250)
        wait(1000)
        wait(1000)
        self.state = self.config.state.standby
