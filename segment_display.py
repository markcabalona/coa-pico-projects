from machine import Pin
from time import sleep

class SegmentDisplay:
    def __init__(self) -> None:
        #display_pins -> form 6 to 13 (pin 13 is dot)
        self.dp_pins = list()
        for pin_num in range(6,14):
            self.dp_pins.append(Pin(pin_num,Pin.OUT))
            
        self.num_patterns = [[1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],
                [1,1,1,1,0,0,1],[0,1,1,0,0,1,1],[1,0,1,1,0,1,1],
                [1,0,1,1,1,1,1],[1,1,1,0,0,0,0],[1,1,1,1,1,1,1],
                [1,1,1,1,0,1,1]]
            
        
    def turn_off(self):
        for i in range(0,8):
            self.dp_pins[i].value(0)


    def count(self):
        self.dp_pins[7].value(1)
        for num_pattern in self.num_patterns:
            #self.turn_off()
            for i in range(7):
                self.dp_pins[i].value(num_pattern[i])
            sleep(1)
        self.turn_off()
        
            
SegmentDisplay().count()