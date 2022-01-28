from machine import Pin, Timer
import time

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
                
                
                

LedLight().blink()
