# LED Sound Responsive Suit

This is the repository for the source code for the Suit-Zero sound-reactive light-up suit. This suit performs audio spectrum analysis to react with animations in real-time to music in almost all settings. The suit will display animations according to different frequency ranges. The code is easily configurable so that it is simple to change what type of animations can be played as a reaction to any given frequency on any given part of the LED strip. For example, if a bass frequency is detected, it is simple to tell the code what animation (e.g., Sparkles, any color line, or meteor rain) and to play the animation at a particular section (e.g., left collar, right back, top part of the left collar, etc.). This type of flexibility allows this code to be configured for many different types of applications, such as coats of all varieties, pants, shirts, dresses, and, with the right power supply, rooms and furniture.

See it working at [YouTube Video](https://youtu.be/8mMCY5qn3_M).

## Getting Started

To use this code, SPI must be enabled on the Raspberry Pi 3+.

Instructions to Enable SPI [here](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/).

You will need WS212B LED strip and/or Neopixels:
[Adafruit LED Strips](https://www.adafruit.com/category/168)
The project uses both Neopixels and off-brand LED strips.

You will also need to utilize the ADC (Analog to Digital) MCP3008 chip and the Adafruit MCP3008 library:
[Adafruit MCP3008](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/mcp3008).

You will also need the 74AHCT125 level shifter to take the 3-volt signal from the Pi and change it to a 5-volt signal for the LEDs:
[Adafruit Level Shifter](https://www.adafruit.com/product/1787?gclid=CjwKCAjw2_LcBRBYEiwA_XVBU8nmLxrknSKjgDB06bWK4gBCG4Vrdn8v7mgsFcpyH4Ho7kmX--aBvBoCJf8QAvD_BwE)
Depending on how you wire the connections, you could easily use any level shifter.

The code requires the rpi_ws281x code as well. Instructions [here](https://www.raspberrypi.org/forums/viewtopic.php?t=98631).

## Instructions

When you want to run the file on boot of the Raspberry Pi:

Edit this file:
/etc/rc.local

At the bottom of this file, paste:
`<path to your repo>/start.sh`
This will trigger the start script to start the program when the Raspberry Pi boots up.

### Flow of Sound Information into LED Display

This program takes audio samples and identifies the various frequencies in the samples and the amplitude at each frequency "bucket." The resolution of the frequency buckets varies with sample size. The more samples, the higher the resolution. This frequency analysis is accomplished by the numpy discrete fast Fourier transformation (DFFT) library and the Raspberry Pi's SPI interface with an analog microphone.

This video has a really good simple tutorial on what FFT is and how it works at a high level.
[YouTube FFT Tutorial](https://www.youtube.com/watch?reload=9&v=mkGsMWi_j4Q)

These frequency samples are then mapped to different animations and are displayed on the LED strips.
![Flow Diagram](https://github.com/cwolfe007/suitzero/blob/master/flowdiagram.png)

### Detailed Flow of the `suit.py` Main Class

This class contains the main file for the program. This orchestrates the processes to take the audio information and translate the information into the LED display. The program utilizes multiprocessing libraries to share data between each process primarily through queues.
![Suit Flow Diagram](https://github.com/cwolfe007/suitzero/blob/master/suitFlow.png)

### Animation Life Cycle

This is the progression of the animations life cycle.
![Animation Life Cycle](https://github.com/cwolfe007/suitzero/blob/master/animationlifecycle.png)

## What's Next

- Separate the LED Animation process from other logic and create a separate queue.
- Add configuration or properties file to make the code more easily configurable.
- Create a UI for configuration.
- Continue to find flaws and shortcomings to make the code even cooler!

