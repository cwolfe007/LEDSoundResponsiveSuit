from animation import Animation
from neopixel import Color
import numpy as np

class MeteorRain(Animation):
    
    def __init__(self,pixelstart,pixelstop,direction,amp=10,name="MeteorRain",color=Color(128,128,128)):
        self.__name = name
        self.__color = color
        self.__meteorsize = 1
        self.__tail = 5 #Modded value (Tail resets every x steps)
        self.__randomDecay = True
        self.__meteortraildecay = 128
        self.__previousFrame = {}
        self.__direction = direction
        Animation.__init__(self,self.__name,pixelstart,pixelstop,direction,pixelstart,color)
        self.__startpos = self._Animation__pixelstart
    

    def fadeToBlack(self,pixel,fadeValue,pixelColor):

        oldColor = pixelColor
        if oldColor > 0:
            w = (oldColor & 0xff000000) >> 24
            r = (oldColor & 0x00ff0000) >> 16
            g = (oldColor & 0x0000ff00) >> 8
            b = (oldColor & 0x000000ff)

            r= 0 if (r<=10) else int(r-(r*fadeValue/256))
            g= 0 if (g<=10) else int(g-(g*fadeValue/256))
            b= 0 if (b<=10) else int(b-(b*fadeValue/256))

            return (pixel,Color(r,g,b))
        else:
            return (pixel,Color(0,0,0))
            

    def animationStep(self):
       

        self._Animation__currentPixelFrame = [] 
        i = self._Animation__currentpos
       
            
        if  super(MeteorRain,self).continueAnimations():
            #Fade brightness for all LEDs one step

                for pixel in self.__previousFrame.iteritems(): #Clear out all of the pixels
                    
                    if  self.__direction: # Up
        
                        if pixel[0] < self.__startpos: #Is this pixel greater than the lasted blacked out pixel?
                           
                            if not self.__randomDecay or (np.random.randint(0,8) > 1):
                                result = self.fadeToBlack(pixel[0],self.__meteortraildecay,pixel[1])
                                
                                if self._Animation__currentpos % self.__tail == 0: 
                                    self.__startpos  = result[0]
                                    self.__previousFrame = {}

                                self.__previousFrame[self.__startpos] = result[1]
                                self._Animation__currentPixelFrame.append(result)
                    else: #Down
                         if pixel[0] > self.__startpos:
                             if not self.__randomDecay or (np.random.randint(0,8) > 1):
                                result = self.fadeToBlack(pixel[0],self.__meteortraildecay,pixel[1])
                                
                                if self._Animation__currentpos % self.__tail == 0: 
                                    self.__startpos  = result[0]
                                    self.__previousFrame = {}
                                    
                                self.__previousFrame[self.__startpos] = result[1]
                                self._Animation__currentPixelFrame.append(result)
                #Draw Meteor
                for j in range(0,self.__meteorsize ):
                    
                    drawpixel = True
                    pixeltoverify = i-(j*self._Animation__countUp)
                    if self._Animation__direction: #Animation is counting up
                        if pixeltoverify > self._Animation__pixelstart:
                            drawpixel = False
                    else:
                        if pixeltoverify < self._Animation__pixelstart:
                            drawpixel = False
                  
    
                      
                    if drawpixel:
                            self._Animation__currentPixelFrame.append((pixeltoverify,self.__color))
                            self.__previousFrame[pixeltoverify] = self.__color
                            self._Animation__lastPixel = pixeltoverify

           
                
        else:
           self._Animation__isFinished  = True
      
        
class MeteorRainRed(MeteorRain):
    def __init__(self,pixelstart,pixelstop,direction,amp=10):
        self.__name = "MeteorRainRed"
        
        self.__color = Color(0,128,0)
        
        MeteorRain.__init__(self,pixelstart,pixelstop,direction,amp,self.__name,self.__color)
        
class MeteorRainGreen(MeteorRain):
    def __init__(self,pixelstart,pixelstop,direction,amp=10):
        self.__name = "MeteorRainGreen"
        
        self.__color = Color(128,0,0)
        
        MeteorRain.__init__(self,pixelstart,pixelstop,direction,amp,self.__name,self.__color)

class MeteorRainBlue(MeteorRain):
    def __init__(self,pixelstart,pixelstop,direction,amp=10):
        self.__name = "MeteorRainBlue"
        
        self.__color = Color(0,0,128)
        
        MeteorRain.__init__(self,pixelstart,pixelstop,direction,amp,self.__name,self.__color)

class MeteorRainPink(MeteorRain):
    def __init__(self,pixelstart,pixelstop,direction,amp=10):
        self.__name = "MeteorRainPink"
        
        self.__color = self.__color = Color(27,207,228)
        
        MeteorRain.__init__(self,pixelstart,pixelstop,direction,amp,self.__name,self.__color)
        
class MeteorRainYellow(MeteorRain):
    def __init__(self,pixelstart,pixelstop,direction,amp=10):
        self.__name = "MeteorRainYellow"
        
        self.__color = Color(255,255,0)
        
        MeteorRain.__init__(self,pixelstart,pixelstop,direction,amp,self.__name,self.__color)        
