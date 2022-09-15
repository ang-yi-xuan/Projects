from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(180)


#Create function get_color() to get input RBG values to be used to display a message
def get_color(color):
    #Allow user to enter RBG values up to 3 times
    count = 3
    while count > 0:
        #Prompt user to enter each RBG value 
        color_str = input("Enter the value of the " + color + \
                          " color for the message(0 to 255):")
        #Reject input value if it is not in the range 0 - 255
        if not (color_str.isnumeric() and 0 <= int(color_str) <=255 ):
            count -= 1
            #Prompt user to enter a value within the range 0 - 255
            print ("Please enter a value from 0 to 255! \n".format(count))
        else: 
            #Return the string parameter "color" from user input 
            return int(color_str)
            
        #Return value 0 if user does not enter a valid value after 3 tries 
        return 0
        
#Get RBG values from user input and display the message in the color specified
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
msg_color = (r_int, g_int, b_int)
sense.show_message("I got it", text_colour = msg_color)