#Mark Cabalona
#BSCS - 2A
#Project 1 (blinking led light)

from machine import Pin, Timer
import time

def main():
    ledLight = LedLight()#initialize ledlight object
    
    #project1 blink
    #uncomment codes below to run the lab 1 !!comment the codes for project1
    ledLight.addLed(Pin(15,Pin.OUT))
    ledLight.blink(duration = 10)#blink for 10 seconds
    
    #end of project1
    
    #lab 1 turn on from L - R, and turn of from R - L
    #uncomment codes below to run the lab 1 !!comment the codes for project1
    #for pin in range(8,16):
    #    ledLight.addLed(Pin(pin,Pin.OUT))
    #ledLight.toggleAllOnebyOne()
    
    #end of lab 1
    
     
    del ledLight#delete the ledlight object
    
class LedLight:
    def __init__(self):
        self.leds = []
        self.timer = Timer()
        
    def addLed(self,led:Pin):
        print("Led added")
        self.leds.append(led)
        
    def blink(self,duration:int = 3)->None:
        '''
            toggle all leds in self.leds at the same time on and off
        '''
        print(f"Blinking for {duration} seconds...") 
        self.timer.init(freq=2.5, mode=Timer.PERIODIC, callback=lambda timer:[led.toggle() for led in self.leds])
        time.sleep(duration)#pause the execution of the program
        self._dispose()#make sure that all leds are turned off
    
    def toggleAllOnebyOne(self):
        '''
            toggle all leds from left to right on, and turn it off from left to right
        '''
        _leds = self.leds
        [self.myToggle(led) for led in _leds]
        _leds.reverse()
        [self.myToggle(led) for led in _leds]
        self._dispose()#make sure that all leds are turned off
        
    def myToggle(self,led:Pin):
        led.toggle()
        time.sleep(1)
        

    #turn off led
    def _dispose(self)->None:
        print("turning lights off...")
        self.timer.deinit()
        for led in self.leds:
            if led.value() == 1:
                time.sleep(1)
                led.toggle()
            


if __name__ == "__main__":
    main()
