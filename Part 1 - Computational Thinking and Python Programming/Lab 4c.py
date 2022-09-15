from sense_hat import SenseHat
import time
import random
from random import randint

sense = SenseHat()

while True:
    red = (255,0,0)
    green = (0,255,0)
    white = (255,255,255)
    yellow = (255,255,0)
    blue = (0, 0, 255)
    black = (0, 0, 255)

    colours = [red, green, white, yellow, blue, black]

    b = white
    y = random.choice(colours)
    g = random.choice(colours)

    image_pixels = [b, b, b, b, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, y, y, y, b, b, b,
                    b, y, b, y, b, y, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, b, b, b, b, b]

    
    turns = [0, 90, 180, 270]
    sense.set_rotation(random.choice(turns))
    sense.set_pixels(image_pixels)
    time.sleep(1)
    sense.clear()