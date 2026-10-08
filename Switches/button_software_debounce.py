# button_software_debounce.py: Implements software debouncing for reliable push-button reads
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.


from machine import Pin
from neopixel import NeoPixel
import time


# =====================================================
# SWITCH SETUP
# =====================================================

switch_0 = Pin(0, Pin.IN, Pin.PULL_UP)
switch_47 = Pin(47, Pin.IN, Pin.PULL_UP)
switch_48 = Pin(48, Pin.IN, Pin.PULL_UP)


# =====================================================
# ONBOARD RGB LED SETUP
# GPIO 7 = LED power
# GPIO 8 = LED data
# =====================================================

led_power = Pin(7, Pin.OUT)
led_power.value(1)

led = NeoPixel(Pin(8, Pin.OUT), 1)

# Start with LED off
led[0] = (0, 0, 0)
led.write()


# =====================================================
# FLAGS
# These tell the main program which switch was pressed
# =====================================================

switch_0_pressed = False
switch_47_pressed = False
switch_48_pressed = False


# =====================================================
# SINGLE INTERRUPT HANDLER
# =====================================================

def switch_handler(pin):

    global switch_0_pressed
    global switch_47_pressed
    global switch_48_pressed

    # GPIO switches are active LOW.
    # We only want to react when a switch is pressed.
    if pin.value() != 0:
        return

    if pin is switch_0:
        switch_0_pressed = True

    elif pin is switch_47:
        switch_47_pressed = True

    elif pin is switch_48:
        switch_48_pressed = True


# =====================================================
# LED PULSE FUNCTION
# =====================================================

def pulse_led(duration):

    # Turn LED on
    led[0] = (30, 30, 30)
    led.write()

    # Keep it on for the requested duration
    time.sleep_ms(duration)

    # Turn LED off
    led[0] = (0, 0, 0)
    led.write()


# =====================================================
# ATTACH INTERRUPTS
# =====================================================

switch_0.irq(
    trigger=Pin.IRQ_FALLING,
    handler=switch_handler
)

switch_47.irq(
    trigger=Pin.IRQ_FALLING,
    handler=switch_handler
)

switch_48.irq(
    trigger=Pin.IRQ_FALLING,
    handler=switch_handler
)


# =====================================================
# MAIN PROGRAM
# =====================================================

print("Q4 started")
print("Switch 0  -> 200 ms pulse")
print("Switch 47 -> 500 ms pulse")
print("Switch 48 -> 1000 ms pulse")


while True:

    # ---------------------------------------------
    # SWITCH 0
    # ---------------------------------------------

    if switch_0_pressed:

        switch_0_pressed = False

        # Simple debounce
        time.sleep_ms(20)

        if switch_0.value() == 0:

            print("Switch 0 pressed")

            pulse_led(200)


    # ---------------------------------------------
    # SWITCH 47
    # ---------------------------------------------

    if switch_47_pressed:

        switch_47_pressed = False

        time.sleep_ms(20)

        if switch_47.value() == 0:

            print("Switch 47 pressed")

            pulse_led(500)


    # ---------------------------------------------
    # SWITCH 48
    # ---------------------------------------------

    if switch_48_pressed:

        switch_48_pressed = False

        time.sleep_ms(20)

        if switch_48.value() == 0:

            print("Switch 48 pressed")

            pulse_led(1000)


    time.sleep_ms(1)