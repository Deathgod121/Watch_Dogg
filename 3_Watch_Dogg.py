import numpy as np
import pyautogui
import time
from pushbullet import Pushbullet
import sys
import cv2

##############################################################################
# PLEASE BE SURE TO CONFIGURE THE BELOW SECTIONS BEFORE RUNNING THIS SCRIPT! #
##############################################################################

## Configure API key for pushbullet
## Eg: API_KEY = "o.UJ237HdguxHnmns8hHozY8iPTVvy"
API_KEY = "<YOUR_PUSH_BULLET_API_KEY>"

## Define the message you want to get.
text = "Your message here :)"

## Define how long to wait before searching again after a match is found in seconds.
wait_interval = 40

## Define how how often to check the screen for comparison in seconds.
refresh_interval = 3

##############################################################################
# PLEASE BE SURE TO CONFIGURE THE ABOVE SECTIONS BEFORE RUNNING THIS SCRIPT! #
##############################################################################

file = sys.argv[1]
pb = Pushbullet(API_KEY)
ready = np.load(file+"_MATCH_FOUND_ARRAY_DO_NOT_REMOVE_ME.npy")

line_no = 0
with open(file, 'r') as values_file:    
    for line in values_file:
        if line_no < 2:
            None
        elif line_no == 2:
            width = int(line)
        elif line_no == 3:
            None
        elif line_no == 4:
            height = int(line)
        elif line_no == 5:
            None
        elif line_no == 6:
            top_offset = int(line)
        elif line_no == 7:
            None
        elif line_no == 8:
            left_offset = int(line)          
        
        line_no = line_no + 1

print("Watch dogg will now watch the screen at the configured coordinates if the screen matches the saved image a alert will be sent to your phone.")
print("")
print("To close you can simply close the window.")
print("")
print("")

while True:
    if cv2.waitKey(1) == ord("q"):
        break
    img = pyautogui.screenshot(region=(left_offset, top_offset, width, height))

    frame = np.array(img)
    comparison = frame == ready
    equal_arrays = comparison.all()

    if equal_arrays:
        push = pb.push_note('', text)
        print("Match Found pausing search for %s seconds." % wait_interval)
        time.sleep(wait_interval)

    time.sleep(refresh_interval)