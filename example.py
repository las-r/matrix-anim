import max7219
import mtxanim
from machine import Pin, SPI

# example for matrix-anim
# this should make a 2x1 line bounce around at the top of the matrix

# made by las-r on github

# led matrix
spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23))
cs = Pin(5, Pin.OUT)

# define animation
frames = [ # just a list of lists of the coordinates of the pixels that should on in each frame
    [(0, 0), (0, 1)],
    [(1, 0), (1, 1)],
    [(2, 0), (2, 1)],
    [(3, 0), (3, 1)],
    [(4, 0), (4, 1)],
    [(5, 0), (5, 1)],
    [(6, 0), (6, 1)],
    [(7, 0), (7, 1)],
    [(6, 0), (6, 1)],
    [(5, 0), (5, 1)],
    [(4, 0), (4, 1)],
    [(3, 0), (3, 1)],
    [(2, 0), (2, 1)],
    [(1, 0), (1, 1)],
]
anim = mtxanim.Anim(frames,                      # frames
                    max7219.Matrix8x8(spi, cs, 1),  # display
                    5                               # brightness (optional, default 5)
                    )

# play animation
anim.play(10,   # fps
          True  # loop (optional, default true)
          )
