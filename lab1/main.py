#Mark Cabalona
#BSCS - 2A
#Project 1 (blinking led light)import time

from machine import Pin

# from potentiometer import Potentiometer
from ledlight import LedLight

def main():
    #project1 blink
    #uncomment code below to run the lab 1 !!comment out the code for project1 'lab1() and potentiometer()'
    #blink()
    #end of project1
    
    #lab 1 turn on from L - R, and turn of from R - L
    #uncomment code below to run the lab 1 !!comment out the code for project1 'blink() and potentiometer()'
    lab1()
    #end of lab 1
   
    
    
#functions to run different projects
def blink()->None:
    '''project1 blink
        turn led on and of for a given duration
    '''
    #initialize ledLight
    ledLight = LedLight()
    ledLight.addLed(Pin(15,Pin.OUT))
    ledLight.blink(duration = 10)#blink for 10 seconds
    #initialize ledlight object
    del ledLight
                
def lab1()->None:
    '''lab 1 turn 8 leds on from L - R, and off from R - L'''
    #initialize ledLight
    ledLight = LedLight()
    for pin in range(8,16):
        ledLight.addLed(Pin(pin,Pin.OUT))
    ledLight.toggleAllOnebyOne()
    #initialize ledlight object
    del ledLight
    
# def potentiometer():
#     '''turn potentiometer to control brightness of led light'''
#     potentiometer = Potentiometer()
#     potentiometer.run()

if __name__ == "__main__":
    main()

