import cv2
import numpy as np
import pyautogui
import sys
import time

work_dir = sys.argv[1]

print("After 10 seconds the application will take a screen shot of the space you confiured in step 1. This will be what we will be looking for to know we found our intended match.")
print("")
input("Press enter to continue.")
print("")
print("")

line_no = 0
with open(work_dir, 'r') as values_file:    
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

count_down = 10
while True:
    time.sleep(1)
    print("Screenshot in %s seconds." % count_down)
    count_down = count_down - 1

    if count_down < 0:
        print("Screenshot taken!")
        print("")
        break

SCREEN_SIZE = (width, height)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

print("This is the caputured image we will use to compare. Press q on the output window to close or press ctrl+c")

img = pyautogui.screenshot(region=(left_offset, top_offset, width, height))
frame = np.array(img)
np.save(work_dir+"_MATCH_FOUND_ARRAY_DO_NOT_REMOVE_ME.npy", frame)
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

while True:
    out.write(frame)
    cv2.imshow("Display Window", frame)

    if cv2.waitKey(1) == ord("q"):
        die = True
        break

cv2.destroyAllWindows()
out.release()
