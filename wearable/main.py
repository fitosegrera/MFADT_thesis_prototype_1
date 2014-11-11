#!/usr/bin/python
#Python controlling Intel Edison
#Created by: fito_segrera
#fii.to

"""
-----------------------------------------------
|Edison PIN  - Breakout PIN  -   WiringX86 PIN|
-----------------------------------------------
 GND         - j19 Pin 3     -      NULL    
 GPIO 44     - j19 Pin 4     -      14
 GPIO 46     - j19 Pin 5     -      16
 GPIO 48     - j19 Pin 6     -      7
 GPIO 131    - j19 Pin 8     -      1
 GPIO 14     - j19 Pin 9     -      18
 GPIO 40     - j19 Pin 10    -      13
 GPIO 43     - j19 Pin 11    -      11
 GPIO 49     - j20 Pin 6     -      8
 GPIO 42     - j20 Pin 9     -      12
 GPIO 41     - j20 Pin 10    -      10
"""

# Import the GPIOEdison class from the wiringx86 module.
#The Module can be downloaded from: https://github.com/emutex/wiring-x86
from wiringx86 import GPIOEdison as GPIO
import pymongo
from pymongo import MongoClient
import time

# Create a new instance of the GPIOEdison class.
# Setting debug=True gives information about the interaction with sysfs.
gpio = GPIO(debug=False)
pin = [1, 7, 8, 10, 11, 12, 13, 14, 16, 18]

# Set pins to be used as an output GPIO pin.
for i in pin:
    print 'Setting up pin %d' % i
    gpio.pinMode(i, gpio.OUTPUT)

####### MONGODB STUFF ########
#Connect to the database at mongolab.com
#client = MongoClient('mongodb://technoxaman:tiger_vs_dragon@ds051640.mongolab.com:51640/thesis_prototype_1')
client = MongoClient('mongodb://192.168.1.107:27017')
db = client.thesis_prototype_1
#connect to the collection
#collection = db.data_consume
###############################

counter = 0
state = 0

try:
    while(True):
        if counter == 20:
            #collection = db.data_consume
            print list(db.data_consume.find().sort({ 'uid', pymongo.DESCENDING}).limit(1))
            global counter
            global state
            #print 'Blinking pin %d now...' % pin[state]
            # Write a state to the pin. ON or OFF.
            gpio.digitalWrite(pin[state], gpio.HIGH)
            #time.sleep(0.5)
            #gpio.digitalWrite(i, gpio.LOW)
            #time.sleep(0.5)
            counter = 0
            state += 1
        counter += 1
        print counter
        time.sleep(0.5)

# When you get tired of seeing the led blinking kill the loop with
#Ctrl-C.
except KeyboardInterrupt:
    for i in pin:
        # Leave the leds turned off.
        print '\nCleaning up...'
        gpio.digitalWrite(i, gpio.LOW)
        # Do a general cleanup. Calling this function is not mandatory.
        gpio.cleanup()