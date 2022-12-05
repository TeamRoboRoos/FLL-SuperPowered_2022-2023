from math import floor
from modules.runify import runify
from threading import Thread
from pybricks.media.ev3dev import Font
from pybricks.parameters import Button, Color
from pybricks.tools import StopWatch, wait


# Class to control running runs
class menu:
    index = 0
    page = 0
    refresh_time = 100
    max_items = 4

    def __init__(self, config, volume):
        # If sound gets too annoying
        self.ev3 = config.ev3
        self.ev3.speaker.set_volume(volume)

        # Gets configuration
        self.config = config

        # Gets menu data from config
        tempMenu = config.menu
        self.pages = config.menu["pages"]
        del config.menu["pages"]

        self.menu = {}

        self.menu["runs"] = tempMenu["runs"]
        self.menu["left"] = tempMenu["left"]

        for page in self.pages:
            if page != "runs" and page != "left":
                temp = [[item.__name__ for item in tempMenu[page]], [runify(func, self.config)
                        for func in tempMenu[page]]]
            elif page == "runs":
                temp = [[item.__qualname__ for item in tempMenu[page]], tempMenu[page]]
            else:
                continue
            self.menu[page] = temp[:]  # type: ignore

        # Sets up font for menu
        font = Font("Terminal", 16, monospace=True)
        self.ev3.screen.set_font(font)

        # Change status light to standby
        self.ev3.light.on(Color.RED)

        # If battery level too low, give a longer beep

        if self.ev3.battery.voltage() < 8100:
            Thread(target=self.ev3.speaker.beep, args=[1500, 2000]).start()
            # self.ev3.speaker.beep(1500, 2000)
        else:
            Thread(target=self.ev3.speaker.beep, args=[1000, 100]).start()
            # self.ev3.speaker.beep(frequency=1000, duration=100)

    # Main control loop
    # Handles button presses
    def update(self):
        # Makes sure index is within bounds of menu
        self.page = self.wrap_index(self.page, self.pages)
        self.index = self.wrap_index(
            self.index, self.menu[self.pages[self.page]][0])

        # Displays all data
        self.displayMenu(self.index, self.page)

        # Makes sure no button is pressed twice
        wait(self.refresh_time)
        self.refresh_time = 100

        # Gets buttons that are pressed
        button = self.ev3.buttons.pressed()

        # Makes sure only one button is pressed
        if len(button) == 1:
            # If middle button, run the run selected
            if Button.CENTER in button:
                self.run(self.menu[self.pages[self.page]]
                         [1][self.index])
                self.index += 1  # At end of run, move to next run

            # Moves up in the menu
            elif Button.UP in button:
                self.index -= 1
                self.refresh_time = 400

            # Moves down in menu
            elif Button.DOWN in button:
                self.index += 1
                self.refresh_time = 400

            # Each run has a corresponding function that can be run through the
            # left button
            elif Button.LEFT in button:
                if self.menu["left"][self.index] != None:
                    self.menu["left"][self.index]()
                else:
                    print("Nothing assigned")
                self.refresh_time = 400

            # Switch pages
            elif Button.RIGHT in button:
                self.page += 1
                self.index = 0
                self.refresh_time = 400

        # If no buttons are press, check if runButton exists and is pressed
        # If true, run the run too
        elif self.config.runButton != None and self.config.runButton.pressed() == True:
            self.run(self.menu[self.pages[self.page]]
                     [1][self.index])
            self.index += 1  # At end of run, move to next run

    def wrap_index(self, idx, theList):
        if idx >= len(theList):
            idx = 0
        elif idx < 0:
            idx = len(theList)-1
        return idx

    # Displays all information on screen
    def displayMenu(self, curr_index, pageIdx):
        self.ev3.screen.clear()
        count = 0
        if floor(curr_index / self.max_items) * self.max_items > 0:
            self.ev3.screen.print("  ...")

        for item in self.menu[self.pages[pageIdx]][0]:
            count += 1
            if count <= floor(curr_index / self.max_items) * self.max_items:
                continue

            if count-1 == curr_index:
                self.ev3.screen.print(">", item)
            else:
                self.ev3.screen.print(" ", item)

            if count >= floor(curr_index / self.max_items) * self.max_items + self.max_items:
                if len(self.menu[self.pages[pageIdx]][0]) > count:
                    self.ev3.screen.print("  ...")
                break
                # if count >= floor(curr_index / self.max_items) * self.max_items + self.max_items + 1:

        self.ev3.screen.print(
            self.config.name, ":", self.ev3.battery.voltage(), end="")

    def displayInfo(self):
        self.ev3.screen.clear()
        for i in self.config.display:
            self.ev3.screen.print(i())

    def infoLoop(self):
        while True:
            self.displayInfo()
            self.config.timer.wait(100)

    # Runs given run
    def run(self, func):
        self.ev3.speaker.beep(frequency=1000, duration=250)

        self.config.state.setState(self.config.state.running)

        # Start run in another thread (in parallel)
        func.start()

        # Update status light
        self.ev3.light.on(Color.GREEN)

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

            self.displayInfo()
            wait(200)

        # Reset
        self.config.stop()
        self.ev3.speaker.beep(frequency=1000, duration=250)
        self.ev3.light.on(Color.RED)
        if self.pages[self.page] == "runs":
            print(self.menu[self.pages[self.page]][0]
                  [self.index], "Took:", timer.time(), "ms")
        self.config.state.setState(self.config.state.standby)
