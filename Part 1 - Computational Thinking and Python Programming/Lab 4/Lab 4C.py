from sense_hat import SenseHat
import time
import random
from random import randint

sense = SenseHat()

while True:
    #Set RBG values for various colours 
    red = (255,0,0)
    green = (0,255,0)
    white = (255,255,255)
    yellow = (255,255,0)
    blue = (0, 0, 255)
    black = (0, 0, 255)

    colours = [red, green, white, yellow, blue, black]

    #Allow the image to automatically switch between random colours 
    b = white
    y = random.choice(colours)
    g = random.choice(colours)

    #Set pixels of the Sense Hat board to show a yellow arrow on a white backgound
    image_pixels = [b, b, b, b, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, y, y, y, b, b, b,
                    b, y, b, y, b, y, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, y, b, b, b, b,
                    b, b, b, b, b, b, b, b]

    #Allow image to rotate in 4 random orientations that are 90 degrees apart
    turns = [0, 90, 180, 270]
    sense.set_rotation(random.choice(turns))
    sense.set_pixels(image_pixels)
    
    #Allow 1 second delay in the program 
    time.sleep(1)
    sense.clear()
    
