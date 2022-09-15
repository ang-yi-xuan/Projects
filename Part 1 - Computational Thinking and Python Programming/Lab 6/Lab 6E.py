from sense_hat import SenseHat
import time
import random

# create_wall(size, wall_width)
# wall_width can be adjusted
def create_wall(size, width):
  redList = [r,r,r,r,r,r,r,r]
  
  if width >= size/2:
    return
  
  for i in range(0,size):
    if i in range(0, width) or i in range(size-width,size):
      board[i] = redList
    else:
      for j in range(0,width):
        board[i][j] = r
        print(size-j)
        board[i][size-1-j] = r
  return

# create random wall
def create_random_wall(size):
  for i in range(15):
    int_1 = random.randint(0,7)
    int_2 = random.randint(0,7)
    board[int_1][int_2] = r if board[int_1][int_2] != w else w

# create a new target
def set_target(size):
  int_1 = random.randint(0,7)
  int_2 = random.randint(0,7)
  board[int_1][int_2] = g if board[int_1][int_2] != w else set_target(8)
  sense.set_pixels(sum(board,[]))
  return int_1, int_2
  
# check whether there is a wall
def check_wall(x,y,new_x,new_y):
  if board[new_y][new_x] != r:
    return new_x, new_y
  elif board[new_y][x] != r:
    return x, new_y
  elif board[y][new_x] != r:
    return new_x, y
  else:
    return x,y

# check the current status: whether white meets green
def check_status(new_x, new_y):
  if board[new_y][new_x] == g:
    return True
  else:
    # cannot use -1, for -1 represents True in python, should use 0 instead
    return False

# Exercise A
def move_marble(pitch,roll,x,y):
  new_x = x #assume no change to start with
  new_y = y #assume no change to start with
  if 1 < pitch < 179 and x != 0:
    new_x -= 1 # move left
  elif 359 > pitch > 179 and x != 7:
    new_x += 1 # move right
  if 1 < roll < 179 and y != 7:
    new_y += 1 # move up
  elif 359 > roll > 179 and y != 0:
    new_y -= 1 # move down
  new_x, new_y = check_wall(x,y,new_x,new_y)
  return new_x, new_y

sense = SenseHat()

b = (0,0,0)
w = (255,255,255)
r = (255,0,0)
g = (0,255,0)

board = [[b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b],
 [b,b,b,b,b,b,b,b] ]

# marble initialize with (2,2) y,x
x = 0
y = 0

board[y][x] = w

# create_wall(board, board_size, wall_width)
create_wall(8, 0)
create_random_wall(8)

board_1D = sum(board,list())

sense.set_pixels(board_1D)

# set initial goal
start = time.time()
y_g, x_g = set_target(8)

# Exercise B
while True:
  # challenge exercise
  if time.time() - start >= 10:
    # change green
    board[y_g][x_g] = b
    sense.set_pixels(sum(board,[]))
    # upadte green coler
    y_g, x_g = set_target(8)
    start = time.time()
  
  orientation = sense.get_orientation()
  pitch = orientation['pitch']
  roll = orientation['roll']

  # Exercise C
  board[y][x] = b
  x,y = move_marble(pitch,roll,x,y)
  
  # check whether white meets green
  if check_status(x,y):
    sense.show_message("yay!!!")
    sense.clear()
    break
  
  board[y][x] = w
  sense.set_pixels(sum(board,[]))
  time.sleep(0.05)