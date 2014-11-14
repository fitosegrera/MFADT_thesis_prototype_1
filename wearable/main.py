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
#import pymongo
#from pymongo import MongoClient
import time
import urllib2

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
#client = MongoClient('mongodb://technoshaman.local:27017')
#client = MongoClient('mongodb://technoshaman.noip.me:4400')
#db = client.thesis_prototype_1
#connect to the collection
#collection = db.data_consume
###############################

counter = 0

try:
    while(True):
        if counter == 10:
            data = urllib2.urlopen("http://192.168.100:8000/data.txt").read()
            print "Received:", data
            #collection = db.data_consume
            #print list(db.data_consume.find().sort({ 'uid', pymongo.DESCENDING}).limit(1))
            global counter
            print "Received:", data
            if data == 1000:
                gpio.digitalWrite(pin[0], gpio.HIGH)
            if data == 2000:
                gpio.digitalWrite(pin[1], gpio.HIGH)
            if data == 3000:
                gpio.digitalWrite(pin[2], gpio.HIGH)
            if data == 4000:
                gpio.digitalWrite(pin[3], gpio.HIGH)
            if data == 5000:
                gpio.digitalWrite(pin[4], gpio.HIGH)
            if data == 6000:
                gpio.digitalWrite(pin[5], gpio.HIGH)
            if data == 7000:
                gpio.digitalWrite(pin[6], gpio.HIGH)
            if data == 8000:
                gpio.digitalWrite(pin[7], gpio.HIGH)
            if data == 9000:
                gpio.digitalWrite(pin[8], gpio.HIGH)
            if data == 10000:
                gpio.digitalWrite(pin[9], gpio.HIGH)
            counter = 0
        counter += 1
        print counter
        time.sleep(1)

# When you get tired of seeing the led blinking kill the loop with
#Ctrl-C.
except KeyboardInterrupt:
    for i in pin:
        # Leave the leds turned off.
        print '\nCleaning up...'
        gpio.digitalWrite(i, gpio.LOW)
        # Do a general cleanup. Calling this function is not mandatory.
        gpio.cleanup()