# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Pybricks Authors

from typing import Collection, Iterable, Optional, Tuple, Union, overload

from .geometry import Axis, Matrix, vector
from .parameters import Button, Color, Direction, Side, Stop, Port


class System:
    def set_stop_button(self, button: Button) -> None: ...
    def shutdown(self) -> None: ...
    def reset_reason(self) -> int: ...
    def name(self) -> str: ...

class DCMotor:
    def __init__(
        self, port: Port, positive_direction: Direction = Direction.CLOCKWISE
    ): ...
    def dc(self, duty: int) -> None: ...
    def stop(self) -> None: ...
    def brake(self) -> None: ...

class Control:
    @overload
    def limits(self) -> Tuple[int, int, int]: ...
    @overload
    def limits(
        self,
        speed: Optional[int] = None,
        acceleration: Optional[int] = None,
        torque: Optional[int] = None,
    ) -> None: ...
    def pid(self) -> Tuple[int, int, int, None, int]: ...
    @overload
    def pid(
        self,
        kp: Optional[int] = None,
        ki: Optional[int] = None,
        kd: Optional[int] = None,
        reserved: Optional[int] = None,
        integral_rate: Optional[int] = None,
    ) -> None: ...
    @overload
    def target_tolerances(self) -> Tuple[int, int]: ...
    @overload
    def target_tolerances(
        self, speed: Optional[int] = None, position: Optional[int] = None
    ) -> None: ...
    @overload
    def stall_tolerances(self) -> Tuple[int, int]: ...
    @overload
    def stall_tolerances(
        self, speed: Optional[int] = None, time: Optional[int] = None
    ) -> None: ...
    def trajectory(
        self,
    ) -> Tuple[int, int, int, int, int, int, int, int, int, int, int, int]: ...
    def stalled(self) -> bool: ...
    def done(self) -> bool: ...

class Motor(DCMotor):
    control: Control
    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
    ): ...
    def angle(self) -> int: ...
    def speed(self) -> int: ...
    def reset_angle(self, angle: int) -> None: ...
    def hold(self) -> None: ...
    def run(self, speed: int) -> None: ...
    def run_time(
        self, speed: int, time: int, then: Stop = Stop.HOLD, wait: bool = True
    ) -> None: ...
    def run_angle(
        self, speed: int, rotation_angle: int, then: Stop = Stop.HOLD, wait: bool = True
    ) -> None: ...
    def run_target(
        self, speed: int, target_angle: int, then: Stop = Stop.HOLD, wait: bool = True
    ) -> None: ...
    def run_until_stalled(
        self, speed: int, then: Stop = Stop.COAST, duty_limit: Optional[int] = None
    ) -> int: ...
    def track_target(self, target_angle: int) -> None: ...

class Speaker:
    @overload
    def volume(self) -> int: ...
    @overload
    def volume(self, volume: int) -> None: ...
    def beep(self, frequency: int = 500, duration: int = 100) -> None: ...
    def play_notes(self, notes: Iterable[str], tempo: int = 120) -> None: ...

class Light:
    def on(self, brightness: int = 100) -> None: ...
    def off(self) -> None: ...
    def blink(self, durations: Collection[int]) -> None: ...
    def animate(self, brightness_values: Collection[int], interval: int) -> None: ...
    def reset(self) -> None: ...

class ColorLight:
    def on(self, color: Optional[Color]) -> None: ...
    def off(self) -> None: ...
    def blink(self, color: Color, durations: Collection[int]) -> None: ...
    def animate(self, colors: Collection[Color], interval: int) -> None: ...
    def reset(self) -> None: ...

class LightArray:
    def __init__(self, n: int): ...
    def on(self, brightness: Union[int,(int, int, int, int)]) -> None: ...
    def off(self) -> None: ...
    def blink(self, durations: Collection[int]) -> None: ...
    def animate(self, brightness_values: Collection[int], interval: int) -> None: ...

class LightMatrix:
    def __init__(self, rows: int, columns: int): ...
    def orientation(self, up: Side) -> None: ...
    def image(self, matrix: Matrix) -> None: ...
    def animate(self, matrices: Collection[Matrix], interval: int) -> None: ...
    def pixel(self, row: int, column: int, brightness: int = 100) -> None: ...
    def off(self) -> None: ...
    def number(self, number: int) -> None: ...
    def char(self, char: str) -> None: ...
    def text(self, text: str, on: int = 500, off: int = 50) -> None: ...
    def reset(self) -> None: ...

class Keypad:
    def pressed(self) -> Tuple[Button]: ...

class Battery:
    def voltage(self) -> int: ...
    def current(self) -> int: ...

class Charger:
    def connected(self) -> bool: ...
    def status(self) -> int: ...
    def current(self) -> int: ...

class SimpleAccelerometer:
    def acceleration(self) -> Tuple[int, int, int]: ...
    def up(self) -> Side: ...

class Accelerometer:
    def neutral(self, top: Axis, front: Axis) -> None: ...
    @overload
    def acceleration(self) -> vector[float, float, float]: ...
    @overload
    def acceleration(self, axis: Axis) -> int: ...
    def tilt(self) -> Tuple[int, int]: ...
    def tapped(self) -> bool: ...
    def shaken(self) -> bool: ...
    def up(self) -> Side: ...

class IMU(Accelerometer):
    def heading(self) -> int: ...
    def reset_heading(self, angle): ...
    @overload
    def gyro(self) -> vector[float, float, float]: ...
    @overload
    def gyro(self, axis: Axis) -> int: ...
