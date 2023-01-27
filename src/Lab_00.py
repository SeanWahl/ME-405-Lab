"""!@file Lab_00.py 
@brief        Increases the brightness of an LED over 5 seconds and loops. 
@author       Nathan Dodd 
@author       Lewis Kanagy 
@author       Sean Wahl 
@date         January 22, 2023 
"""

import time

def led_setup():  
    """!@brief Sets up the pin, timer, and timer channel for an LED to be used."""

    # Pin object for the other end of the LED. 
    pinA0 = pyb.Pin (pyb.Pin.board.PA0, pyb.Pin.OUT_PP) #sets up pin for PWM 
    # Timer object associated with pinA0, to be used with PWM. 
    tim2 = pyb.Timer (2, freq=20000) # set frequency of PWM 
    global ch2   
    # Channel 2 of timer 2, to be used with the LED’s PWM. 
    ch2 = tim2.channel (1, pyb.Timer.PWM_INVERTED, pin=pinA0) #declare ch2   

 

def led_brightness(n):  
    """!@brief    Sets the LED’s PWM to the value specified. 
    @details      Given an input n, will set the LED’s PWM to an inverted percentage of n, thereby setting the LED’s brightness to n%. 
    @param n The percent brightness of the LED. """
    ch2.pulse_width_percent (n)   # Set the brightness of the LED to n% 
    time.sleep(0.05)              # Pause for 50 milliseconds 

if __name__ == "__main__":        # create loop to run blinking 
    led_setup()                   # run led_setup() 
    while True:                   # while loop to constantly run program 
        for n in range (101):     # count n up from 0 to 101 
            led_brightness(n)     # run led_brightness 
