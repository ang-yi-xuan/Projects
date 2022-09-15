from sense_hat import SenseHat
sense = SenseHat()

b = (0,0,0)
w = (255,255,255)

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
board [y][x]=w # a white marble

board_1D=sum(board,[]) # Convert 2-dimensional data structure to 1-dimensional list
print(board_1D) # For code debugging
sense.set_pixels(board_1D) # Display a marble on the (2,2) point on the RPi board