from sense_hat import SenseHat
import time 
sense = SenseHat()

b = [0,0,0]
w = [255,255,255]

board = [ [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b],
          [b,b,b,b,b,b,b,b] ]
          
          
y=2 # y coordinate of marble
x=2 # x coordinate of marble

# Function move_marble checks the pitch value and the x coordinate 
# to determine whether to move the marble in the x-direction
# Similarly, it checks the roll value and the y coordinate to 
# determine whether to move the marble in the y-direction

def move_marble(pitch, roll, x, y):
    new_x = x # Assume no change to start with 
    new_y = y # Assume no change to start with
    if 1 < pitch < 179 and x != 0:
        new_x -= 1 # Move Left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1 # Move Right

    if 1 < roll < 179 and y!= 7:
        new_y += 1 # Move Up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1 # Move Down 

# Compute new coordinate of the marble based on the roll and pitch 
# values gathered from the board

    return new_x, new_y 

# Allow marble to move according to the tilt of the RPi along the 
# x and y axes by detecting the roll and pitch of the board

while True:
    pitch = sense.get_orientation() ['pitch']
    roll = sense.get_orientation() ['roll']
    x,y = move_marble(pitch,roll,x,y)
    board[y][x] = w
    sense.set_pixels(sum(board, []))
    time.sleep(0.05)
    board[y][x] = b


