# ws2812_blink.py: makes the rgb led blink in red
# This is the ubiquitous blink program you find on all embedded systems
# This particular program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
# Copyright (c) U. Raich, 1.9.2026
# The program is part of the IMU course at the University of Cape Coast, Ghana
# It is released under the MIT lice

from s3minipro import rgb_led, RGB_POWER
from machine import Pin
from time import sleep_ms

# switch the power for the LED on
led_power = Pin(RGB_POWER,Pin.OUT)
led_power.on()

# these functions switch the led to red or off
def led_on():
    rgb_led(32,0,0)
    
def led_off():
    rgb_led(0,0,0)

# blink until the program is interrupted
# the frequency is 1 Hz
# before terminating, switch the led off
while True:
    try:
        led_on()
        sleep_ms(500)
        led_off()
        sleep_ms(500)
    except KeyboardInterrupt:
        # switch the led and its power pin off
        led_off()
        led.power.off()
        break
