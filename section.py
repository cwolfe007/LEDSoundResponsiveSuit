from stepanimation import * #simple step animation
from sparkleanimation import *
from meteorrain import *
from ampanimation import *
import time

class Section:

	def __init__(self,name,pixelstart,pixelstop,direction,anime):
		
		if not direction:
			self.__pixelstart = pixelstart
			self.__pixelstop = pixelstop
		else:
			self.__pixelstart = pixelstop
			self.__pixelstop = pixelstart
		self.__name = name
		self.__allowedanimationLifeSpan = 1.0 #How long something is allowed to live in the queue

		self.__temp = [] #Temperary Stack to hold animations
		self.__direction = direction #Boolean False = Down, True = Up
		self.__animationStack = []
		self.__currentFrame =[]
		self.__stackLimit=10
		self.__stackSize = 0
		self.__sinerotations = 2520.0

		self.__sineTable = []
		SAMPLES = 256 #Shades of value
		OUTMAX = 255


		for sample in range(SAMPLES):
		    angle = (sample * self.__sinerotations) / SAMPLES
		    sine = math.sin(math.radians(angle))
		    rescaled = int(round(((sine + 1) * OUTMAX ) / 2.0))	  
		    self.__sineTable.append(rescaled) 	  

		if(anime == "Step"):
			
			self.__animationStack.append(Step(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable))
			self.__stackSize +=1 
		elif(anime == "StepRed"):
			
			self.__animationStack.append(StepRed(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable))
			self.__stackSize +=1 
		elif (anime == "StepBlue"):
			
			self.__animationStack.append(StepBlue(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable))
			self.__stackSize +=1 
		elif (anime == "StepGreen"):
			
			self.__animationStack.append(StepBlue(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable))
			self.__stackSize +=1 
		elif (anime == "MeteorRain"):
			
			self.__animationStack.append(MeteorRain(self.__pixelstart, self.__pixelstop,self.__direction))
			self.__stackSize +=1 
		elif (anime == "MeteorRainRed"):
			
			self.__animationStack.append(MeteorRainRed(self.__pixelstart, self.__pixelstop,self.__direction))
			self.__stackSize +=1 
		self.__isAnimationCompleted = False

	def getpixelStart(self):
		return self.__pixelstart
	def getpixelStop(self):
		return self.__pixelstop


	
	def removeAnimation(self):
		
		self.__animationStack.pop()

	
	def getName(self):
		return self.__name
	
	def addAnimation(self,anime,amp=0,range=(0,0)):

		if not self.__stackSize >= self.__stackLimit:
		#Select what Animation to be played (anime = animation name)
			
			if(anime == "Step"):
				animation = Step(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif(anime == "StepRed"):
				animation = StepRed(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif(anime == "StepLightRed"):
				animation = StepLightRed(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)				
			elif (anime == "StepBlue"):
				animation = StepBlue(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif (anime == "StepLightBlue"):
				animation = StepLightBlue(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)				
			elif (anime == "StepGreen"):
				animation = StepGreen(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif (anime == "StepLightGreen"):
				animation = StepGreen(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)				
			elif (anime == "StepPink"):
				animation = StepPink(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif (anime == "StepYellow"):
				animation = StepYellow(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif (anime == "StepOrange"):
				animation = StepOrange(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)
			elif (anime == "StepRose"):
				animation = StepRose(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)								
			elif (anime == "StepPurple"):
				animation = StepPurple(self.__pixelstart, self.__pixelstop,self.__direction,self.__sineTable,amp)								
			elif (anime == "Sparkle"):
				animation = Sparkle(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "SparkleRed"):
				animation = SparkleRed(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "SparkleGreen"):
				animation = SparkleGreen(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "SparkleBlue"):
				animation = SparkleBlue(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "MeteorRain"):
				animation = MeteorRain(self.__pixelstart, self.__pixelstop,self.__direction)
                        elif (anime == "MeteorRainRed"):
				animation = MeteorRainRed(self.__pixelstart, self.__pixelstop,self.__direction)
		        elif (anime == "MeteorRainGreen"):
				animation = MeteorRainGreen(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "MeteorRainBlue"):
				animation = MeteorRainBlue(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "MeteorRainPink"):
				animation = MeteorRainPink(self.__pixelstart, self.__pixelstop,self.__direction)
			elif (anime == "MeteorRainYellow"):
				animation = MeteorRainYellow(self.__pixelstart, self.__pixelstop,self.__direction)										
			elif (anime == "AmpAnimation"):
				animation = AmpAnimation(range[0], range[1],self.__direction,amp)	
			elif (anime == "AmpAnimationRed"):
				animation = AmpAnimationRed(range[0], range[1],self.__direction,amp)
			elif (anime == "AmpAnimationGreen"):
				animation = AmpAnimationGreen(range[0], range[1],self.__direction,amp)
			elif (anime == "AmpAnimationBlue"):
				animation = AmpAnimationBlue(range[0], range[1],self.__direction,amp)
			elif (anime == "AmpAnimationWhite"):
				animation = AmpAnimationWhite(range[0], range[1],self.__direction,amp)	 						
			else:
				raise ValueError("ANIMATION NOT FOUND")
			
			self.__animationStack.append(animation)
			self.__stackSize +=1
			
			return True #indicate that Animation was sucessfully added


	def getNextAnimation(self):


		currentPos = self.__pixelstart # Set the current postion in the LED strip to the first pixel
		
		self.__currentFrame =[] #Reset the animation frame
		
		while self.__animationStack: #while stack is not empty
			 animation = self.__animationStack.pop()  #Set the next animation to be played
			 animation.setPixelStart(currentPos)#Set the latest pixel postion in the animations
			 animation.animationStep() # This Calculates the value of the pixel(s) for the current frame
			 for p in animation.currrentPixelFrame(): #Append the list of pixels to be sent to the queue
			 	self.__currentFrame.append(p)
			 	
			 currentPos=animation.getLastPixel() #set the current position to the latest pixel in the frame, this will tell the next animation where to start
			 
			 self.__temp.append(animation) # put the animation into a queue for processing
			 return True #Indicate that this section has an animation to play 
		else:
			return False #Indicate that this section has no animations to play
	
	
	def getStackSize(self):
		return self.__stackSize
	
	def playAnmimation(self):
		
		 return self.__currentFrame


	def progressAnimations(self): #iterate through animations in queue and continue the animattions if not finished or remove the finished ones


		curenttime = time.clock()
		while self.__temp: #While Temp
			animation = self.__temp.pop()

			animationlifespan = curenttime - animation.getAnimationStartTime() #Check to see how long the animation has been alive, if past the duration of life span, remove it from the queue
			
			if not animation.animationFinished() and ( animationlifespan < self.__allowedanimationLifeSpan):
				animation.progressFrame()

				self.__animationStack.append(animation)
			else:
				self.__stackSize -=1 

	def animationCompleteCheck(self):
		self.__isAnimationCompleted = self.__animation.isFinished

		return self.__isAnimationCompleted

