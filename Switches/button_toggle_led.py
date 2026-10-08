# button_toggle_led.py: Toggles the onboard RGB LED when the button is pressed
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.


from machine import Pin
import time


# -------------------------------------------------
# SET UP THE THREE SWITCHES
# -------------------------------------------------

switch_0 = Pin(0, Pin.IN, Pin.PULL_UP)
switch_47 = Pin(47, Pin.IN, Pin.PULL_UP)
switch_48 = Pin(48, Pin.IN, Pin.PULL_UP)


# -------------------------------------------------
# SINGLE INTERRUPT HANDLER
# -------------------------------------------------

def switch_handler(pin):

    # Determine which Pin object caused the interrupt

    if pin is switch_0:
        switch_number = 0

    elif pin is switch_47:
        switch_number = 47

    elif pin is switch_48:
        switch_number = 48

    else:
        return


    # Read the state
    state = pin.value()


    # Remember:
    # 0 = pressed
    # 1 = released

    if state == 0:
        print("Switch", switch_number, ": PRESSED")

    else:
        print("Switch", switch_number, ": RELEASED")


# -------------------------------------------------
# PRINT INITIAL STATES
# -------------------------------------------------

print("Initial states:")


if switch_0.value() == 0:
    print("Switch 0: PRESSED")
else:
    print("Switch 0: RELEASED")


if switch_47.value() == 0:
    print("Switch 47: PRESSED")
else:
    print("Switch 47: RELEASED")


if switch_48.value() == 0:
    print("Switch 48: PRESSED")
else:
    print("Switch 48: RELEASED")


# -------------------------------------------------
# ATTACH INTERRUPTS
# -------------------------------------------------

switch_0.irq(
    trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
    handler=switch_handler
)

switch_47.irq(
    trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
    handler=switch_handler
)

switch_48.irq(
    trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING,
    handler=switch_handler
)


# -------------------------------------------------
# KEEP PROGRAM RUNNING
# -------------------------------------------------

while True:
    time.sleep_ms(100)