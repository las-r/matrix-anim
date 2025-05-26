import max7219
from mtxanim import Anim, strToFrame
from machine import Pin, SPI

spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
cs = Pin(5, Pin.OUT)

frames = [
    strToFrame("..####../.#....#./#......./#......./#......./#......./.#....#./..####../"),
    strToFrame("..####../.#....#./#......#/#......#/#......#/#......#/.#....#./......../"),
    strToFrame("..####../.#....#./.......#/.......#/.......#/.......#/.#....#./..####../"),
    strToFrame("......../.#....#./#......#/#......#/#......#/#......#/.#....#./..####../")
]

Anim(frames, max7219.Matrix8x8(spi, cs, 1)).play(8)
