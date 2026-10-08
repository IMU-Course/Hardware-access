# jpg_test.py: Displays a JPG image on the ST7789 screen
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.


import st7789
import tft_config

# Create the display object using the hardware settings. 
# The '0' argument typically sets the initial display rotation (0 degrees)
tft = tft_config.config(0)

# Initialize the ST7789 display controller
tft.init()

# Print a status message to the serial console (REPL) for debugging
print("Displaying JPG...")

# Decode and display the JPG image on the screen
tft.jpg(
    "/jpg/bigbuckbunny-128x128.jpg",  # The path to the uploaded image file in the flash memory
    0,                                # X-coordinate (start drawing at the far left edge)
    0,                                # Y-coordinate (start drawing at the very top edge)
    st7789.SLOW                       # Rendering mode: SLOW reads the image in chunks to save RAM
)

# Print a confirmation message to the serial console once the rendering is complete
print("JPG displayed")