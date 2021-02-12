#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in February 2021
# Program blinks an LED with incremental delay


import board
import digitalio
import time

import constants


def main():
    # Blinks a light on and off every second

    led = digitalio.DigitalInOut(board.D13)
    led.direction = digitalio.Direction.OUTPUT
    
    blink_time = 1

    while True:
        led.value = True
        time.sleep(blink_time)
        led.value = False
        time.sleep(constants.DELAY_TIME)
        
        blink_time += constants.TIME_INCREMENT


# Makes this file run as the main file of the program, and runs menu_scene()
if __name__ == "__main__":
    main()
