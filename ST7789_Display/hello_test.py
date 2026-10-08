# hello_test.py: Initializes the ST7789 display and prints a text message
#
# This program uses the hardware definition file "s3minipro.py" to
# define the hardware connections on the Lolin esp32-s3 mini pro board.
#
# Copyright (c) James Buabeng Inkoom, October 2026
# The program is part of the IMU course at the University of Cape Coast, Ghana.
# It is released under the MIT license.


import sys
import st7789
import tft_config

# Add the fonts folder to the system path so the interpreter can locate the font files
sys.path.insert(0, "/fonts")

# Load the specific 8x8 pixel VGA font
import vga1_8x8 as font

# Create the display object using the hardware settings defined in tft_config
tft = tft_config.config()

# Initialize the ST7789 display controller
tft.init()

# Clear the entire screen by filling it with a black background
tft.fill(st7789.BLACK)

# Print the text to the display using the specified parameters
tft.text(
    font,            # The font module loaded above
    "Hello!",        # The string of text to display
    40,              # X-coordinate (horizontal position from the left)
    60,              # Y-coordinate (vertical position from the top)
    st7789.WHITE,    # Text color (White)
    st7789.BLACK     # Text background color (Black)
)