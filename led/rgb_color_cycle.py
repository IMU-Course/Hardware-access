# rgb_color_cycle.py: Cycles the WS2812B RGB LED through different colors
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.

from machine import Pin, Timer
import neopixel
import micropython
import time

LED_POWER = 7
LED_DATA = 8

MAX_INTENSITY = 32

# Turns LED power on
power = Pin(LED_POWER, Pin.OUT)
power.value(1)

# Sets up NeoPixel
led = neopixel.NeoPixel(Pin(LED_DATA), 1)


# RGBs helper
def rgb(r, g, b):
    led[0] = (g, r, b)
    led.write()


# Current LED state
led_on = False


# Function that changes the LED
def toggle_led(dummy):
    global led_on

    led_on = not led_on

    if led_on:
        # RED
        rgb(MAX_INTENSITY, 0, 0)
    else:
        # OFF
        rgb(0, 0, 0)


# Timer interrupt callback
def timer_callback(timer):
    # Schedule the LED update outside the interrupt
    micropython.schedule(toggle_led, 0)


# Creates timer
timer = Timer(0)

try:

    # Toggle every 500 ms
    timer.init(
        period=500,
        mode=Timer.PERIODIC,
        callback=timer_callback
    )

    # Keep program running
    while True:
        time.sleep(1)

finally:

    # Disable timer
    timer.deinit()

    # LED off
    rgb(0, 0, 0)

    # LED power off
    power.value(0)

    print("Timer disabled")
    print("LED and power OFF")