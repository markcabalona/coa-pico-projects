from machine import Pin
from time import sleep
from dht11 import DHT11

pin = Pin(14,Pin.OUT)

dht11 = DHT11(pin)

while True:
    print(f"Temperature is {dht11.temperature}")
    sleep(1)
    print(f"Temperature is {dht11.temperature}")
    sleep(1)