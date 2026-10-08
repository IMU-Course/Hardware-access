# nasa_clock_test.py: Displays a NASA-themed clock on the ST7789 screen
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.

import time
# Import the display driver and the board's hardware configuration
import st7789
import tft_config

# Create the display object, setting the initial screen rotation (0 degrees)
tft = tft_config.config(0)

# Initialize the ST7789 display controller
tft.init()

# Start an infinite loop to keep the animation running continuously
while True:
    # Loop through the numbers 1 to 25 (range stops right before 26)
    for i in range(1, 26):
        # Format the filename dynamically. {:02d} ensures numbers are zero-padded 
        # to two digits (e.g., nasa01.jpg, nasa02.jpg ... nasa25.jpg)
        filename = "/clock_128x128/nasa{:02d}.jpg".format(i)

        # Print the current filename to the serial console so you can track the progress
        print("Displaying:", filename)

        # Decode and render the current JPG image to the screen
        tft.jpg(
            filename,      # The dynamically generated path to the image file
            0,             # X-coordinate (start at the far left)
            0,             # Y-coordinate (start at the very top)
            st7789.SLOW    # Rendering mode: SLOW reads the image in chunks to save RAM
        )

        # Pause the program for 2 seconds before loading the next image in the sequence
        time.sleep(2)