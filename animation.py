from neopixel import Color
import sys
import pydevd
import time


class Animation(object):
    # This is the class to track animation state

    def __init__(
        self,
        name,
        pixelstart,
        pixelstop,
        direction,
        currentpos,
        color=Color(128, 128, 128),
    ):  # Direction = False:Down Or True:UpS
        self.__tic = time.clock()
        self.__name = name

        if not direction:  # Down
            self.__countUp = 1  # Direction for count down
        else:
            self.__countUp = -1  # Direction for count up
        self.__pixelstop = pixelstop  # What pixel to stop on
        self.__pixelstart = pixelstart  # What pixel to start on
        self.__color = color  # the color of the pixel being lit
        self.__isFinished = False  # is the animation complete
        self.__currentPixelFrame = []
        self.__direction = direction
        self.__lastPixel = self.__pixelstart
        self.__currentpos = self.__pixelstart  # current position of something
        self.__pixel = self.__pixelstart  # what pixel is being lit

    def animationStep(self):
        self.__currentPixelFrame = []  # blank out old information about frame

        if (
            self.__currentpos == self.__pixelstop
        ):  # Ensure that animation only applies the target pixels
            for pixel in range(self.__pixelstart, self.pixelstop, 1, self.__countUp):
                if (
                    pixel == self.__currentpos
                ):  # Set colors in section that are need for animation
                    self.__pixel = pixel
                    targetPixel = (self.__pixel, self.__color)
                    self.__currentPixelFrame.append(targetPixel)
                self.__lastPixel = pixel

        else:
            self.isFinished = True  # once out of pixel range finish animation

    def getAnimationStartTime(self):
        return self.__tic

    def getLastPixel(self):
        return self.__lastPixel

    def getName(self):
        return self.__name

    def progressFrame(self):  # progress to the animations next pixel set
        self.__currentpos += 1 * self.__countUp

    def printCompletionTime(self):
        print(
            "animation completed in "
            + str(time.clock() - self.__tic)
            + "s to go accross "
            + str(self.__pixelstop - self.__pixelstart)
        )

    def continueAnimations(self):
        if not self.__direction:  # LED strip is in the down direction
            if self.__currentpos < self.__pixelstop:
                return True
            else:
                return False
        else:  # LED string is in the up direction
            if self.__currentpos > self.__pixelstop:
                return True
            else:
                return False

    def getCurrentPos(self):
        return self.__currentpos

    def setCurrentPos(self, currentPos):
        self.__currentpos = currentPos

    def animationFinished(self):
        return self.__isFinished

    def currrentPixelFrame(self):
        return self.__currentPixelFrame

    def getPixelStart(self):
        return self.__pixelstart

    def setPixelStart(self, pixel):
        self.__pixelstart = pixel

    def getPixelStop(self):
        return self.__pixelstop

    def setPixelStop(self, pixel):
        self.__pixelstop = pixel
