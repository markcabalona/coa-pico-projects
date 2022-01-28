#Mark Cabalona
#BSCS - 2A
#Project 1 (blinking led light)import time

from machine import Pin

from potentiometer import Potentiometer


def main():
    potentiometer()
    
    
def potentiometer():
    '''turn potentiometer to control brightness of led light'''
    potentiometer = Potentiometer()
    potentiometer.run()

if __name__ == "__main__":
    main()

