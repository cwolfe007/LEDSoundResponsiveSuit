# LED Sound Repsponsive Suit 
This is the repository for the source code for the Suit-Zero sound reactive light up suit. This suit performs audio spectrum analysis to react with animations in realtime to music in almost all settings. The suit will display animations according to different frequency ranges. The code is easily configurable to so that it is simple to change what type of animations can be played as a reaction to any given frequency on any given part of the LED strip. For example, if a bass frequency is detected, it is simple to tell the code what animation( e.g. Sparkles, any color line, or meteor rain) and to play the animation at a particular section (e.g. left collar, right back, top part of left collar, etc.). This type of flexibility allows this code to be configured for many different types of applications, such as: coats of all varieties, pants, shirts, dresses, and, with the right power supply, rooms and furniture. 

View the Album of the Suit in action at TomorrowLand 2018:
https://photos.app.goo.gl/o8Hv4VvpwqH7Gr9x6

## Getting Started 
To use this code SPI must be enabled on the Raspberry pi 3+ 

Instructions to Enable SPI here
https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/ 

You will need WS212B LED strip and/or Neopixels:
https://www.adafruit.com/category/168
I used both neopixels and off brand LED strips for this project

You will also need to utilize the ADC (Anlog to Digital) MCP3008 chip and the Adafruit MCP3008 library
https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008

You will also need the 74AHCT125 level shifter to take the 3volt signal from the pi and change it too a 5 volt signal for the LEDs 
https://www.adafruit.com/product/1787?gclid=CjwKCAjw2_LcBRBYEiwA_XVBU8nmLxrknSKjgDB06bWK4gBCG4Vrdn8v7mgsFcpyH4Ho7kmX--aBvBoCJf8QAvD_BwE
Depending on how you wire the conenctions you could easily use any level shifter

The code requires the rpi_ws281x code as well. Instructions here 
https://www.raspberrypi.org/forums/viewtopic.php?t=98631

## Instructions:

When you want to run the file on boot of the Raspberry pi

Edit this file: 
/etc/rc.local

at the bottom of this file paste:
<path to your repo>/start.sh
This will trigger the start script to start the program when the raspberry pi boots up

### Flow of sound information into LED display

This program takes audio samples and identifies the various frequencies in the samples and the amplitude at each frequency "bucket"
There resolution of the freuqncy buckets varies with sample size. The more samples, the higher the resolution. 
This frequency analysis is accomplished by the numpy disctrete fast fouier  transformation (DFFT) library and the raspberry pi's SPI interface with an analog microphone. 

This video has a really good simple tutorial on what FFT is and how it works at a high level.
https://www.youtube.com/watch?reload=9&v=mkGsMWi_j4Q

These frequency samples are then mapped to different animations and are displayed on the LED strips. 
![alt text](https://github.com/cwolfe007/suitzero/blob/master/flowdiagram.png)

### Detailed flow of the suit.py main class

This class contains the main file for the program. This orchastrates the processes to take the audio information and translate the information into the LED display. The program utilizes multiprocessing libraries to share data between each process primarily through queues. 

![alt text](https://github.com/cwolfe007/suitzero/blob/master/suitFlow.png)



### Animation Life Cycle

This is the progression of the animations life cycle

![alt text](https://github.com/cwolfe007/suitzero/blob/master/animationlifecycle.png)

## What's next
- Seperate the LED Animation process from other logic and create seperate queue 
- Add configuration or properties file to make the code more easily configurable 
- Create a UI for configuration
- Coninue to find flaws and shortcomings to make the code even cooler!

