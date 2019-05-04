
# Spectrum Analyzer Code Author: Caleb Wolfe
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import numpy as np




class SpectrumAnalyzer:

    def __init__(self,smprate=44100,senistivity=100.0,samplesize=1024):
            	
            	self.__samplerate =smprate
            	
            	self.__peaksample = senistivity
            	
            	self.__samplesArraySize = samplesize #sample size for the audio batch to be analyzed
            	self.__buckets = []
    	    	# Hardware SPI configuration:
    		SPI_PORT   = 0
    		SPI_DEVICE = 0
    		spid = SPI.SpiDev(SPI_PORT, SPI_DEVICE)
    		spid.set_clock_hz(self.__samplerate)
    		self.__mcp = Adafruit_MCP3008.MCP3008(spi=spid)

    		



    def __calculate_levels(self,inputarray): 
       
       darray = np.array(inputarray, dtype='float')
       fourier=np.fft.rfft(darray) #apply discrete FFT 
       fftusable= fourier[:self.__samplesArraySize-1] #Remove items past Nyquist limit
       power = np.abs(fftusable) #convert the complex numbers to real numbers
       nyqquistadjustment= (power*2)/ (1024*self.__samplesArraySize) #Adjust the values to find actual amplitude (1024 is the max range of voltage)  
       result = nyqquistadjustment
       
       self.__fft = result

    def __readmicval(self):
        value = self.__mcp.read_adc(0)
        return value


    
    def __getvals(self):


        subbassbucket = []
        bassbucketlow = []
        bassbuckethigh = []
        
        lowmid1bucket = []
        lowmid2bucket = []
        lowmid3bucket = []
        lowmid4bucket = []
     
        mid1bucket = []
        mid2bucket = []
        mid3bucket = []
        mid4bucket = []
        midbuckethigh = []
        highbucketlow = []
        highbuckethigh = []

        amps = []
        currentpos = 0
        #find the values of the amplitudes to each bucket
        for a in self.__fft: #append amplitudes  to buckets
    	    amp = a * 10000 # make values more managable (Lower decible setting, changed to 10000 for experimentaion with quieter db levels
    		
    	    frq = self.__freqarray[currentpos] # get the current frequency
            
#     	    
            if (amp > self.__peaksample): #this applies senistivity levels to ignor non signifigant amplitudes
               
                if  (frq > 20 and frq < 60): # and p in range(0,3) :
              	     amp = (amp+50)%256
           	     subbassbucket.append(amp)
                elif (frq >= 60 and frq < 155): # and p in range(3,5):
                         bassbucketlow.append(amp)
                elif (frq >= 155 and frq < 250):
                        bassbuckethigh.append(amp)
         	
                elif (frq >= 250 and frq < 313):	
                     lowmid1bucket.append(amp)
                elif (frq >= 313 and frq <  376): # and p in range(5,9):
                     lowmid2bucket.append(amp)
                elif (frq >= 376 and frq <  439): # and p in range(5,9):
                     lowmid3bucket.append(amp) 
                elif (frq >= 439 and frq <  500): # and p in range(5,9):
                     lowmid4bucket.append(amp)                        
                
                elif  (frq >= 500 and frq < 875):
                 	mid1bucket.append(amp)
                elif frq >= 875 and frq < 1250:
                    mid2bucket.append(amp)
                elif (frq >= 1250 and frq < 1625): # and p in range(9,12):
                     mid3bucket.append(amp)
                elif (frq >= 1625 and frq < 2000): # and p in range(9,12):
                     mid4bucket.append(amp)                 
                elif (frq >= 2000 and frq < 3000): #and p in range(12,15):
                 	highbucketlow.append(amp)
                elif (frq >= 3000 and frq < 4000): #and p in range(12,15):
                     highbuckethigh.append(amp)

            currentpos += 1
        self.__buckets = [np.mean(subbassbucket),np.mean(bassbucketlow),np.mean(bassbuckethigh),np.mean(lowmid1bucket),np.mean(lowmid2bucket),np.mean(lowmid3bucket),np.mean(lowmid4bucket),np.mean(mid1bucket),np.mean(mid2bucket),np.mean(mid3bucket),np.mean(mid4bucket),np.mean(highbucketlow),np.mean(highbuckethigh) ]

        

    def getSpectrumBuckets(self):
        return self.__buckets


    def analyzeSpectrum(self):

        tic = time.clock()
        data = [self.__readmicval()  for x in range(self.__samplesArraySize)]
        toc = time.clock()
        fft = self.__calculate_levels(data)
        processtime = toc-tic 
        
        stimestep = processtime /self.__samplesArraySize #average step time

        self.__freqarray = np.fft.fftfreq(self.__samplesArraySize,stimestep) #get freq steps

        self.__getvals()

print('Reading MCP3008 values, press Ctrl-C to quit...')


