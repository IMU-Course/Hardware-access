# png_slideshow.py: Cycles through a slideshow of PNG images on the display
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.

import time
# Import the display driver module and the board's hardware configuration
import st7789
import tft_config

# Create the display object, setting the initial screen rotation to 0 degrees
tft = tft_config.config(0)

# Initialize the ST7789 display controller
tft.init()

# Define a list containing the file paths of the PNG images 
# previously uploaded to the board's flash memory
images = [
    "/png/bigbuckbunny-128x128.png",
    "/png/logo-128x128.png",
    "/png/logo-64x64.png",
    "/png/alien.png",
]

# Start an infinite loop to keep the slideshow running continuously
while True:
    # Iterate through each image path in the list
    for image in images:
        # Clear the display by filling it with a black background 
        # to prevent previous images from ghosting underneath smaller PNGs
        tft.fill(st7789.BLACK)

        # Print the current image path to the serial console for tracking
        print("Displaying:", image)

        # Decode and render the current PNG image to the screen
        tft.png(
            image,   # The path to the current image in the loop
            0,       # X-coordinate (start at the far left)
            0        # Y-coordinate (start at the very top)
        )

        # Pause the program for 3 seconds before loading the next image
        time.sleep(3)