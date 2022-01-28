from machine import Pin,SPI,ADC
import max7219
from utime import sleep

MAX7219_NUM = 4
MAX7219_INVERT = False
MAX7219_SCROLL_DELAY  = 0.15

spi =SPI(0)
display = max7219.Matrix8x8(spi=spi, cs=Pin(5), num=MAX7219_NUM)

p = MAX7219_NUM * 8
to_volts = 3.3 / 65535
temper_sensor = ADC(4)

while True:
    temper_volts = temper_sensor.read_u16()
    celsius_degrees = 27 -(temper_volts -0.706) / 0.001721
    text = 'Temp:'+str(round(celsius_degrees,2))

    
    for p in range(MAX7219_NUM * 8, len(text) * -8 -1, -1):
        display.fill(MAX7219_INVERT)
        display.text(text, p, 1, not MAX7219_INVERT)
        
        
        display.show()
        
        sleep(MAX7219_SCROLL_DELAY)
        
        
        
        
        
        
        
        
        
        
        
        