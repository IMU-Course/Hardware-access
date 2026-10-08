# button_simple_read.py: Reads the state of the tactile switch and prints it to the console
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.


from machine import Pin
import time

# Configure the three switches
switch_0 = Pin(0, Pin.IN, Pin.PULL_UP)
switch_47 = Pin(47, Pin.IN, Pin.PULL_UP)
switch_48 = Pin(48, Pin.IN, Pin.PULL_UP)

# Store them together
switches = {
    0: switch_0,
    47: switch_47,
    48: switch_48
}

# Remember the previous state of each switch
previous_states = {}

# Print initial states
print("Initial switch states:")

for number, switch in switches.items():
    state = switch.value()
    previous_states[number] = state

    if state == 0:
        print("Switch", number, ": PRESSED")
    else:
        print("Switch", number, ": RELEASED")


# Continuously monitor switches
while True:

    for number, switch in switches.items():

        current_state = switch.value()

        # Has the state changed?
        if current_state != previous_states[number]:

            if current_state == 0:
                print("Switch", number, ": PRESSED")
            else:
                print("Switch", number, ": RELEASED")

            # Save the new state
            previous_states[number] = current_state

    time.sleep_ms(100)