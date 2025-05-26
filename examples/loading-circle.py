import max7219
from mtxanim import Anim, strToFrame
from machine import Pin, SPI

# example for matrix-anim
# this should make a loading circle

# made by las-r on github

# lcd matrix
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
cs = Pin(5, Pin.OUT)

# define frames using str to frame func
frames = [
    strToFrame("..####../.#....#./#......./#......./#......./#......./.#....#./..####../"),
    strToFrame("..####../.#....#./#......#/#......#/#......#/#......#/.#....#./......../"),
    strToFrame("..####../.#....#./.......#/.......#/.......#/.......#/.#....#./..####../"),
    strToFrame("......../.#....#./#......#/#......#/#......#/#......#/.#....#./..####../")
]

# create and play animation
Anim(frames, max7219.Matrix8x8(spi, cs, 1)).play(8)
