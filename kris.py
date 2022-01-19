#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017-18 Richard Hull and contributors
# License: https://github.com/rm-hull/luma.led_matrix/blob/master/LICENSE.rst
# Github link: https://github.com/rm-hull/luma.led_matrix/
import RPi.GPIO as GPIO
import time
# Import all the modules 
import re
import time
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

from pibuttons import ButtonMatrix

def main(msg, cascaded, block_orientation, rotate):
    
    # create matrix device
    serial = spi(port=0, device=1, gpio=noop())
    device = max7219(serial, cascaded=cascaded or 1, block_orientation=block_orientation, rotate=rotate or 0)
    # debugging purpose
    print("[-] Matrix initialized")

    # print hello world on the matrix display
    # debugging purpose
    print("[-] Printing: %s" % msg)
    show_message(device, msg, fill="white", font=proportional(CP437_FONT), scroll_delay=0.1)

def button():
    buttons = ButtonMatrix()
    try:
        while(True):
            pressed = buttons.check(1 / 10)
            if any([ any([ p for p in r ]) for r in pressed ]):
                if pressed[0][0] != 0:
                    main(msg = "did you watch the new comic book movie?    it was very graphic", cascaded=1, block_orientation=90, rotate=0)
                if pressed[0][1] != 0:
                    main(msg = "why did the bike refuse to move?    it was two tired", cascaded=1, block_orientation=90, rotate=0)
                if pressed[0][2] != 0:
                    main(msg = "i got hit in the head with a soda can.    im ok, it was a soft drink", cascaded=1, block_orientation=90, rotate=0)
                if pressed[0][3] != 0:
                    main(msg = "i can't tell if i like my new blender.    it keeps giving me mixed results", cascaded=1, block_orientation=90, rotate=0)
                    
    except KeyboardInterrupt:
        GPIO.cleanup()



if __name__ == "__main__":
    
    # cascaded = Number of cascaded MAX7219 LED matrices, default=1
    # block_orientation = choices 0, 90, -90, Corrects block orientation when wired vertically, default=0
    # rotate = choices 0, 1, 2, 3, Rotate display 0=0°, 1=90°, 2=180°, 3=270°, default=0
   
    try:
        main(msg = "hello. press buttons 1, 2, 3, or 4 to hear a joke", cascaded=1, block_orientation=90, rotate=0)
        button()
    except KeyboardInterrupt:
        pass
