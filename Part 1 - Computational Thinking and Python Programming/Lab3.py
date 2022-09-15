from sense_hat import SenseHat
sense = SenseHat()

color_msg = (255,255,0)
color_bg = (255,255,255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

color_str = input ("Choose text colour (Red/Blue/Green) : ")

try: 

   if color_str== "Red" :

      result_color = red

   elif color_str== "Blue":

      result_color = blue

   elif color_str== "Green":
    
      result_color = green

except:

    print("Error! Wrong color selected! Please choose either Red/Blue/Green")

while color_str!= ("Red" or "Blue" or "Green") :
    print("Wrong colour selected! Please choose either Red/Blue/Green")
    color_str = input ("Choose text colour (Red/Blue/Green) : ")

    if color_str== "Red" :
            result_color = red
        
    elif color_str== "Blue" :
            result_color = blue 
        
    elif color_str=="Green" :
            result_color = green
            
                         

speed_str = input("Enter the speed of your text from 0.0 - 1: ")
speed =float(speed_str)
sense.set_rotation(180)

sense.show_message("This is fun!!!", text_colour=(result_color),
back_colour =(color_bg), scroll_speed= speed)

sense.clear()