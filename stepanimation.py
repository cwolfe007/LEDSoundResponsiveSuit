from animation import Animation
from neopixel import *


class Step(Animation):
    def __init__(
        self,
        pixelstart,
        pixelstop,
        direction,
        sinetable,
        amp=5.0,
        name="Step",
        color=Color(128, 128, 128),
    ):
        self.__name = name
        self.__color = color
        newval = int(amp)
        self.__traverse = 1
        self.__sinetablepos = 0
        self.__sineTable = sinetable
        self.__trail = newval % 6

        Animation.__init__(
            self, self.__name, pixelstart, pixelstop, direction, pixelstart, color
        )

    def pulse(self, pixel, pixelColor):
        if self.__sinetablepos >= len(self.__sineTable):
            self.__traverse = -1
            self.__sinetablepos = len(self.__sineTable) - 1
        elif self.__sinetablepos <= 0:
            self.__traverse = 1
            self.__sinetablepos = 0
        w = (pixelColor & 0xFF000000) >> 24
        r = (pixelColor & 0x00FF0000) >> 16
        g = (pixelColor & 0x0000FF00) >> 8
        b = pixelColor & 0x000000FF

        val = self.__sineTable[self.__sinetablepos]

        r = 0 if (r <= 10) else int(r - (r * val / 256))
        g = 0 if (g <= 10) else int(g - (g * val / 256))
        b = 0 if (b <= 10) else int(b - (b * val / 256))
        self.__sinetablepos += 1 * self.__traverse
        return (pixel, Color(r, g, b))

    def animationStep(self):
        self._Animation__currentPixelFrame = []

        continuestep = True
        if self._Animation__direction:
            start = self._Animation__pixelstart + (
                self._Animation__currentpos - self._Animation__pixelstart
            )  # Where to start drawing pixels
            stop = start + (
                self.__trail * self._Animation__countUp
            )  # where to stop drawing pixels
            if stop <= self._Animation__pixelstop:
                continuestep = False
        else:
            start = self._Animation__currentpos  # Where to start drawing pixels
            stop = start + (
                self.__trail * self._Animation__countUp
            )  # where to stop drawing pixels
            if stop >= self._Animation__pixelstop:
                continuestep = False

        if super(Step, self).continueAnimations() and continuestep:
            for pixel in range(start, stop, self._Animation__countUp):
                # pydevd.settrace('192.168.1.19',port=5678)

                targetpixel = self.pulse(pixel, self._Animation__color)

                self._Animation__lastPixel = pixel
                self._Animation__currentPixelFrame.append(targetpixel)

        else:
            self._Animation__isFinished = True


class StepRed(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepRed"

        self.__color = Color(0, 128, 0)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepGreen(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepGreen"

        self.__color = Color(128, 0, 0)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepLightGreen(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepLightGreen"

        self.__color = Color(0, 153, 153)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepBlue(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepBlue"

        self.__color = Color(0, 0, 128)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepPink(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepPink"

        self.__color = Color(0, 200, 75)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepYellow(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepYellow"

        self.__color = Color(255, 255, 0)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepLightBlue(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepLightBlue"

        self.__color = Color(204, 51, 255)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepPurple(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepPurple"

        self.__color = Color(0, 75, 200)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepRose(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepRose"

        self.__color = Color(51, 100, 51)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepOrange(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepOrange"

        self.__color = Color(75, 255, 0)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )


class StepLightRed(Step):
    def __init__(self, pixelstart, pixelstop, direction, sinetable, amp=5):
        self.__name = "StepLightRed"

        self.__color = Color(51, 255, 51)

        Step.__init__(
            self,
            pixelstart,
            pixelstop,
            direction,
            sinetable,
            amp,
            self.__name,
            self.__color,
        )
