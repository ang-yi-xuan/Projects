from sense_hat import SenseHat

#Import textcolor.py program and run the get_color() function
from textcolor import get_color

sense = SenseHat()
sense.set.rotation(180)

#------------------------------------------------------------------

#Get RBG values from get_color() function and display the message in the color specified
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
msg_color = (r_int, g_int, b_int)
sense.show_message("I got it", text_colour = msg_color)