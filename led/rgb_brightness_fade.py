# rgb_brightness_fade.py: Fades the WS2812B RGB LED in and out
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.


from machine import Pin
import neopixel
import time

LED_POWER = 7
LED_DATA = 8

MAX_INTENSITY = 32

# Enable RGB LED power
power = Pin(LED_POWER, Pin.OUT)
power.value(1)

# Set up NeoPixel
led = neopixel.NeoPixel(Pin(LED_DATA), 1)


# RGB helper
def rgb(r, g, b):
    led[0] = (g, r, b)
    led.write()


try:
    while True:

        # BLUE
        print("BLUE")
        rgb(0, 0, MAX_INTENSITY)
        time.sleep(1)

        # CYAN = Green + Blue
        print("CYAN")
        rgb(0, MAX_INTENSITY, MAX_INTENSITY)
        time.sleep(1)

        # GREEN
        print("GREEN")
        rgb(0, MAX_INTENSITY, 0)
        time.sleep(1)

        # YELLOW = Red + Green
        print("YELLOW")
        rgb(MAX_INTENSITY, MAX_INTENSITY, 0)
        time.sleep(1)

        # MAGENTA = Red + Blue
        print("MAGENTA")
        rgb(MAX_INTENSITY, 0, MAX_INTENSITY)
        time.sleep(1)

        # RED
        print("RED")
        rgb(MAX_INTENSITY, 0, 0)
        time.sleep(1)

        # WHITE = Red + Green + Blue
        print("WHITE")
        rgb(
            MAX_INTENSITY,
            MAX_INTENSITY,
            MAX_INTENSITY
        )
        time.sleep(1)

        # OFF
        print("OFF")
        rgb(0, 0, 0)
        time.sleep(1)

finally:

    rgb(0, 0, 0)
    power.value(0)

    print("LED and power OFF")