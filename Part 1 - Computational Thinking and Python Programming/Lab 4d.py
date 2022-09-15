from sense_hat import SenseHat
import time
import random
import sys 
from random import randint

sense = SenseHat()

#Set RBG values for various colours 
r = (255,0,0)
g = (0,255,0)
b = (255,255,255)

sense.clear()

#Set pixels of the Sense Hat board to show a green arrow on a white backgound
img1= [b, b, b, b, b, b, b, b,
       b, b, b, g, b, b, b, b,
       b, b, g, g, g, b, b, b,
       b, g, b, g, b, g, b, b,
       b, b, b, g, b, b, b, b,
       b, b, b, g, b, b, b, b,
       b, b, b, g, b, b, b, b,
       b, b, b, b, b, b, b, b]

#Set pixels of the Sense Hat board to show a red arrow on a white backgound
img2= [b, b, b, b, b, b, b, b,
       b, b, b, r, b, b, b, b,
       b, b, r, r, r, b, b, b,
       b, r, b, r, b, r, b, b,
       b, b, b, r, b, b, b, b,
       b, b, b, r, b, b, b, b,
       b, b, b, r, b, b, b, b,
       b, b, b, b, b, b, b, b]


#Define a function to set the image that will be shown on the display
def put_arrow(img):
  x=0
  sense.clear()
  for a in range (0,8):
     for b in range (0,8):
       sense.set_pixel(b,a,img[x])
       x += 1

#Rotate the orientation of the display image by 90 degrees 
rotate = [0,90]

#Allow user to continue playing the game when the arrow is pointing up 
continue_game = True 

#Allow the image to rotate randomly 
while continue_game: 
    put_arrow(img1)
    rotation = random.randint(0,1)
    sense.set_rotation(rotate[rotation])
    time.sleep(1)
    
    #Detect the amount of G-force acting on each axis x and y 
    acceleration = sense.get_accelerometer_raw()
    x = round(acceleration['x'])
    y = round(acceleration['y'])

    #Show image 2 and end the game 
    if rotation > 0:
      
      if x>=0:
        put_arrow(img2)
        notLose=False

      else:
        if y < 1:
          put_arrow(img2)
          notLose=False
          break