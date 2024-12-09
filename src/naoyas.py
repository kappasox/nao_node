#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# naoyas.py
# a sample (?) code of bme280 and amibeit.io .
#

# MIT License
# 
# Copyright (c) 2024 kappasox (Michiharu Takemoto <takemoto.development@gmail.com>)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# 

import os
from os.path import join, dirname

from time import sleep

import board 
# pip install smbus2
from adafruit_bme280 import basic as adafruit_bme280
# pip install adafruit-circuitpython-bme280
import adafruit_ssd1306
# pip install adafruit-circuitpython-ssd1306

from PIL import Image, ImageDraw, ImageFont
#font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

import ambient
# pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git

from dotenv import load_dotenv
# pip install python-dotenv

WIDTH = 128
HEIGHT = 64
BORDER = 5


if ('__main__' == __name__):
    print('wait 60 sec.')
    sleep(60) # if python starts too early, raspberry pi does not connect to the network.

    i2c = board.I2C()   # uses board.SCL and board.SDA
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)
    bme280.sea_level_pressure = 1013.30 #2024/10/24 00:43
    print("Temperature: %0.1f C" % bme280.temperature)
    print("Humidity: %0.1f %%" % bme280.relative_humidity)
    print("Pressure: %0.1f hPa" % bme280.pressure)
    print("Altitude = %0.2f meters" % bme280.altitude)
    sleep(3)

    ssd1306 = adafruit_ssd1306.SSD1306_I2C(width=WIDTH, height=HEIGHT, i2c=i2c, addr=0x3c)

    image = Image.new("1", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)

    dotenv_file = join(dirname(__file__), '.env')
    load_dotenv(verbose=True, dotenv_path=dotenv_file)
    my_channel_id = os.environ.get('CHANNEL_ID')
    my_write_key = os.environ.get('WRITE_KEY')
    ambi = ambient.Ambient(my_channel_id, my_write_key) 

    while True:
        try:
            try:
                tempe = bme280.temperature
                humid = bme280.relative_humidity
                press = bme280.pressure
                altit = bme280.altitude
                print(tempe)
            except:
                print('Error in using BME280!')
                sleep(5)

            try:
                text_t = "Tempe: %0.1f C" % tempe
                text_h = "Humid: %0.1f %%" % humid
                text_p = "Prs: %0.1f hPa" % press

                draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)
                draw.text((0, 0), text_t, font=font, fill=255)
                draw.text((0, 16), text_h, font=font, fill=255)
                draw.text((0, 32), text_p, font=font, fill=255)
                ssd1306.image(image)
                ssd1306.show()
                sleep(1)
            except:
                print('Error in using SSD1306!')
                sleep(5)


            try:
                r = ambi.send({"d1": tempe, "d2": humid, "d3": press, "d4": altit})
            except:
                print('Error: accessing ambient.io!')
                sleep(30)

            sleep(5)

        except KeyboardInterrupt:
            print()
            print('Ctrl-C is pressed.')
            break

    print('Program ends.')


		

