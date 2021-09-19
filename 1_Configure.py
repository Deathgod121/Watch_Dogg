import cv2
import numpy as np
import pyautogui
import sys
import time

work_dir = sys.argv[1]

die = False
while True:
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
   
    SCREEN_SIZE = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))

    read_file_count = 0

    while True:
        img = pyautogui.screenshot(region=(left_offset, top_offset, width, height))
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("Display Window", frame)
        time.sleep(0.025)
        read_file_count = read_file_count + 1
        if read_file_count == 25:
            break

        if cv2.waitKey(1) == ord("q"):
            die = True
            break

    cv2.destroyAllWindows()
    out.release()

    if die:
        break