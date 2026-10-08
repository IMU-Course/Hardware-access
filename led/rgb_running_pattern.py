# rgb_running_pattern.py: Displays a running light pattern on the WS2812B RGB LED
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

# Enable LED power
power = Pin(LED_POWER, Pin.OUT)
power.value(1)

# Set up RGB LED
led = neopixel.NeoPixel(Pin(LED_DATA), 1)


# RGB helper
def rgb(r, g, b):
    led[0] = (g, r, b)
    led.write()


try:
    while True:

        # ===============================
        # Increase intensity: 0 -> 32
        # ===============================

        for intensity in range(0, MAX_INTENSITY + 1):

            rgb(
                intensity,
                intensity,
                intensity
            )

            print("Intensity:", intensity)

            time.sleep(0.05)


        # ===============================
        # Decrease intensity: 31 -> 0
        # ===============================

        for intensity in range(MAX_INTENSITY - 1, -1, -1):

            rgb(
                intensity,
                intensity,
                intensity
            )

            print("Intensity:", intensity)

            time.sleep(0.05)


finally:

    rgb(0, 0, 0)
    power.value(0)

    print("LED and power OFF")