import time

# made by las-r on github
# mit license
# v1.0

# animation class
class Anim:
    # init
    def __init__(self, frames, display, brightness=5):
        self.frames = frames
        self.display = display
        self.display.brightness(brightness)
    
    # play function
    def play(self, fps, loop=True):
        delay = 1 / fps
        if loop:
            while True:
                for f in self.frames:
                    self.showFrame(f)
                    time.sleep(delay)
        else:
            for f in self.frames:
                self.showFrame(f)
                time.sleep(delay)
    
    # show a frame
    def showFrame(self, frame):
        self.display.fill(0)
        for x, y in frame:
            self.display.pixel(x, y, 1)
        self.display.show()
