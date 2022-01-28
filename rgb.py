# MARK CABALONA
# BSCS - 2A

import machine
import utime

#enum
class LedColor():
    RED = (1,0,0)
    GREEN = (0,1,0)
    BLUE = (0,0,1)
    RED_GREEN = (1,1,0)
    RED_BLUE = (1,0,1)
    BLUE_GREEN = (0,1,1)
    WHITE = (1,1,1)
    

class RGB:
    def __init__(self):
        self.led_red = machine.Pin(10, machine.Pin.OUT)
        self.led_green = machine.Pin(11, machine.Pin.OUT)
        self.led_blue = machine.Pin(14, machine.Pin.OUT)
        self.button_red = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
        self.button_black = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
        
    def _toggle(self,color:LedColor = LedColor.GREEN):
        self.led_red.value(color[0])
        self.led_green.value(color[1])
        self.led_blue.value(color[2])
    
    def blink(self,loop_count:int = 1,interval:float = .5):
        for count in range(loop_count):
            self._toggle(LedColor.RED)
            print("red")
            utime.sleep(interval)
            
            self._toggle(LedColor.GREEN)
            print("green")
            utime.sleep(interval)
            
            self._toggle(LedColor.BLUE)
            print("blue")
            utime.sleep(interval)
            
            self._toggle(LedColor.RED_GREEN)
            print("red + green")
            utime.sleep(interval)
            
            self._toggle(LedColor.RED_BLUE)
            print("red + blue")
            utime.sleep(interval)
            
            self._toggle(LedColor.BLUE_GREEN)
            print("green + blue")
            utime.sleep(interval)
            
            self._toggle(LedColor.WHITE)
            print("white(R + G + B)")
            utime.sleep(interval)
            
            self._turnOff()
            print("off")
            utime.sleep(interval)
            
    def switch_test(self):
        #default value of red is 0
        #default value of black is 1
        while True:
            if self.button_red.value() == 1:
                print("red")
                
            if self.button_black.value() == 0:
                print("black")
            utime.sleep(.5)
            
    def int_handler(self,pin:machine.Pin)->None:
        self.button_red.irq(handler=None)
        print("Interupt detected!")
        #self._toggle(LedColor.RED)
        self.led_red.value(1)
        self.led_green.value(0)
        utime.sleep(4)
        self.led_red.value(0)
        self.button_red.irq(handler=self.int_handler)
        
    def interupts(self):
        self.button_red.irq(trigger=machine.Pin.IRQ_RISING, handler=self.int_handler)
        while True:
            if self.button_black.value() == 0:#exit
                return
            self.led_green.toggle()
            utime.sleep(1)
        
            
    def switch_led(self):
        while True:
            if self.button_red.value() == 1:#exit
                break
            if self.button_black.value() == 0:
                self._toggle(LedColor.RED)
                utime.sleep(1)
                self._toggle(LedColor.GREEN)
                utime.sleep(1)
                self._toggle(LedColor.BLUE)
                utime.sleep(1)
                self._turnOff()
                
        
            
    def _turnOff(self):
        self.led_red.value(0)
        self.led_green.value(0)
        self.led_blue.value(0)
            
        
rgb= RGB()
rgb._turnOff()
rgb.blink(loop_count = 10, interval = .5)
#rgb.swith_test()
#rgb.interupts()
#rgb.switch_led()

rgb._turnOff()

