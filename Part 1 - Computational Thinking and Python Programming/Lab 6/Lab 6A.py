from sense_hat import SenseHat
import time
sense = SenseHat()
sense.set_rotation(180)

while True:
    pitch = sense.get_orientation()['pitch'] # Detect pitch (y-axis) of RPi board
    roll = sense.get_orientation()['roll'] # Detect roll (x-axis) of RPi board
    print("pitch {0} roll {1}".format(round(pitch,0), round(roll,0))) # Print corresponding values of pitch and roll of RPi board
    time.sleep (0.05)