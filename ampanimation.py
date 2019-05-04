from animation import Animation
from neopixel import *


class AmpAnimation(Animation):
         def __init__(self,pixelstart,pixelstop,direction,amp,color,name="AmpAnimation",duration=3):
            self.__name = name
            self.__duration = duration
            self.__amp = int(amp)
            self.__color = color

            Animation.__init__(self,self.__name,pixelstart,pixelstop,direction,pixelstart,self.__color)
        
         def animationStep(self):

             
             if self.__duration >= 0 :
                
                for p in range(self._Animation__pixelstart, self._Animation__pixelstop):
                    
                    self._Animation__pixel = p
                    targetpixel = (self._Animation__pixel,self._Animation__color)
                    self._Animation__currentPixelFrame.append(targetpixel)
             else:
                self._Animation__isFinished  = True       
             
         def progressFrame(self): #progress to the animations next pixel set
             self.__duration -= 1
            
             
class AmpAnimationRed(AmpAnimation):
        def __init__(self,pixelstart,pixelstop,direction,amp,duration=1):
            self.__name = "AmpAnimationRed"
            self.__duration = duration
            self.__amp = int(amp) 
            self.__color = color=Color(0,self.__amp%255,0)

            AmpAnimation.__init__(self,pixelstart,pixelstop,direction,self.__amp,self.__color,self.__name,duration)

class AmpAnimationGreen(AmpAnimation):
        def __init__(self,pixelstart,pixelstop,direction,amp,duration=1):
            self.__name = "AmpAnimationGreen"
            self.__duration = duration
            self.__amp = int(amp) 
            self.__color = color=Color(self.__amp%255,0,0)

            AmpAnimation.__init__(self,pixelstart,pixelstop,direction,self.__amp,self.__color,self.__name,duration)

class AmpAnimationBlue(AmpAnimation):
        def __init__(self,pixelstart,pixelstop,amp,direction,duration=1):
            self.__name = "AmpAnimationBlue"
            self.__duration = duration
            self.__amp = int(amp) 
            self.__color = color=Color(0,0,self.__amp%255)

            AmpAnimation.__init__(self,pixelstart,pixelstop,direction,self.__amp,self.__color,self.__name,duration)
            
class AmpAnimationWhite(AmpAnimation):
        def __init__(self,pixelstart,pixelstop,direction,amp,duration=1):
            self.__name = "AmpAnimationBlue"
            self.__duration = duration
            self.__amp = int(amp) 
            self.__color = color=Color(self.__amp%255,self.__amp%255,self.__amp%255)

            AmpAnimation.__init__(self,pixelstart,pixelstop,direction,self.__amp,self.__color,self.__name,duration)