# ir_led_transmit.py: Transmits signals using the onboard IR LED
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

# Delay determines how quickly colors change
DELAY = 0.05

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

        # =====================================
        # 1. RED -> YELLOW
        #
        # Red stays at 32
        # Green increases 0 -> 32
        # =====================================

        for green in range(0, MAX_INTENSITY + 1):

            rgb(
                MAX_INTENSITY,
                green,
                0
            )

            time.sleep(DELAY)


        # =====================================
        # 2. YELLOW -> GREEN
        #
        # Green stays at 32
        # Red decreases 32 -> 0
        # =====================================

        for red in range(MAX_INTENSITY, -1, -1):

            rgb(
                red,
                MAX_INTENSITY,
                0
            )

            time.sleep(DELAY)


        # =====================================
        # 3. GREEN -> CYAN
        #
        # Green stays at 32
        # Blue increases 0 -> 32
        # =====================================

        for blue in range(0, MAX_INTENSITY + 1):

            rgb(
                0,
                MAX_INTENSITY,
                blue
            )

            time.sleep(DELAY)


        # =====================================
        # 4. CYAN -> BLUE
        #
        # Blue stays at 32
        # Green decreases 32 -> 0
        # =====================================

        for green in range(MAX_INTENSITY, -1, -1):

            rgb(
                0,
                green,
                MAX_INTENSITY
            )

            time.sleep(DELAY)


        # =====================================
        # 5. BLUE -> MAGENTA
        #
        # Blue stays at 32
        # Red increases 0 -> 32
        # =====================================

        for red in range(0, MAX_INTENSITY + 1):

            rgb(
                red,
                0,
                MAX_INTENSITY
            )

            time.sleep(DELAY)


        # =====================================
        # 6. MAGENTA -> RED
        #
        # Red stays at 32
        # Blue decreases 32 -> 0
        # =====================================

        for blue in range(MAX_INTENSITY, -1, -1):

            rgb(
                MAX_INTENSITY,
                0,
                blue
            )

            time.sleep(DELAY)


finally:

    # Turn LED off
    rgb(0, 0, 0)

    # Turn LED power off
    power.value(0)

    print("LED and power OFF")