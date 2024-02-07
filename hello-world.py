#!/usr/bin/env python3

# Import only the modules for LCD communication
from library.lcd.lcd_comm import Orientation
from library.lcd.lcd_comm_rev_a import LcdCommRevA
from library.lcd.lcd_comm_rev_b import LcdCommRevB
from library.lcd.lcd_comm_rev_c import LcdCommRevC
from library.lcd.lcd_comm_rev_d import LcdCommRevD

lcd_comm = LcdCommRevB(com_port="AUTO",
                       display_width=320,
                       display_height=480)
lcd_comm.Reset()
lcd_comm.InitializeComm()  # Mandatory!

lcd_comm.SetBrightness(level=90)
lcd_comm.SetBackplateLedColor(led_color=(255, 255, 255))  # Optional
lcd_comm.SetOrientation(orientation=Orientation.PORTRAIT)  # Optional

background = "res/backgrounds/mona-lisa-2.png"
lcd_comm.DisplayBitmap(background)

lcd_comm.DisplayText(" Hello \n World! ", x=5, y=150,
                     font="roboto/Roboto-Italic.ttf",
                     font_size=100,
                     font_color=(0, 0, 255),
                     background_color=(255, 0, 0))
