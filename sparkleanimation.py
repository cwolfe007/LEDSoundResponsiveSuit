from animation import Animation
from neopixel import *
import numpy as np


class Sparkle(Animation):
    def __init__(
        self,
        pixelstart,
        pixelstop,
        direction,
        name="Sparkle",
        color=Color(128, 128, 128),
    ):
        self.__name = name
        self.__color = color
        self.__pixelstart = pixelstart
        self.__pixelstop = pixelstop
        self.__duration = 3
        self.__pos = 0
        if direction:  # Prevent low>high error in numpy randint
            self.__pixelstart = pixelstop
            self.__pixelstop = pixelstart
        Animation.__init__(
            self,
            self.__name,
            self.__pixelstart,
            self.__pixelstop,
            direction,
            pixelstart,
            color,
        )

    def animationStep(self):
        self._Animation__currentPixelFrame = []

        if self.__pos < self.__duration:
            for pixel in range(0, 2):
                choice = np.random.randint(self.__pixelstart, self.__pixelstop)
                if choice is not 0:
                    self._Animation__pixel = int(choice)
                    targetpixel = (self._Animation__pixel, self._Animation__color)
                    self._Animation__currentPixelFrame.append(targetpixel)
            self.__pos += 1
            # self._Animation__currentpos +=1
        else:
            self._Animation__isFinished = True


class SparkleRed(Sparkle):
    def __init__(self, pixelstart, pixelstop, direction):
        self.__name = "SparkleRed"
        self.__color = Color(0, 128, 0)
        Sparkle.__init__(
            self, pixelstart, pixelstop, direction, self.__name, self.__color
        )


class SparkleGreen(Sparkle):
    def __init__(self, pixelstart, pixelstop, direction):
        self.__name = "SparkleGreen"
        self.__color = Color(128, 0, 0)
        Sparkle.__init__(
            self, pixelstart, pixelstop, direction, self.__name, self.__color
        )


class SparkleBlue(Sparkle):
    def __init__(self, pixelstart, pixelstop, direction):
        self.__name = "SparkleBlue"
        self.__color = Color(0, 0, 128)
        Sparkle.__init__(
            self, pixelstart, pixelstop, direction, self.__name, self.__color
        )
