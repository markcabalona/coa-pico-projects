#Mark Cabalona
#BSCS - 2A
#Project 1 (blinking led light)

from machine import Pin, Timer
import time

def main():
    ledLight = LedLight()#initialize ledlight object
    ledLight.addLed(led = Pin(15,Pin.OUT))#add a led
    ledLight.blink(duration = 5)#blink for 5 secons
    ledLight.dispose()#stops blinking
    del ledLight#delete the ledlight object
    
class LedLight:
    def __init__(self):
        self.led = list(Pin)
        self.timer = Timer()
        
    #ayaw gumana bakit haha
    def __del__(self):
        self.dispose()
    
    def addLed(self,Pin led):
        self.led.append(led)
        
    def blink(self,duration:int = 3)->None:
        print(f"Blinking for {duration} seconds...")
        self.timer.init(freq=2.5, mode=Timer.PERIODIC, callback=lambda timer:led.toggle() for led in self.led)
        time.sleep(duration)#default is 3seconds
        
    #always turn off 
    def dispose(self)->None:
        print("turning lights off...")
        self.timer.deinit()
        if self.led.value() == 1:
            time.sleep(1)
            self.led.toggle()
            


if __name__ == "__main__":
    main()
