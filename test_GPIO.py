# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 15:35:08 2019

@author: jlchang
"""

import RPi.GPIO as GPIO
in1_pin=36#一般桶
in2_pin=38#塑膠桶
in3_pin=40#紙類桶
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(in2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(in3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    print("一般桶定位狀態：{:}".format(GPIO.input(in1_pin)))
    print("塑膠桶定位狀態：{:}".format(GPIO.input(in2_pin)))
    print("紙類桶定位狀態：{:}".format(GPIO.input(in3_pin)))
    print("")

