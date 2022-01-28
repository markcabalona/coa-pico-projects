from machine import ADC, Pin, PWM
import time

class Potentiometer:
    def __init__(self):
        self.pmw = PWM(Pin(15))
        self.adc = ADC(Pin(26))
        
    def run(self):
        while(True):
            duty = self.adc.read_u16()
            self.pwm.duty_u16(duty)