from machine import Pin
from utime import sleep

sensor = Pin(15,Pin.IN)
led = Pin(25,Pin.OUT)

def led_on() -> None:
    led.value(1)
    
def led_off() -> None:
    led.value(0)
    
def scan() -> bool:
    return sensor.value() == 1
        
while True:
    if scan():
        led_on()
        print("MOTION DETECTED")
        sleep(1)
    led_off()

    

