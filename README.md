# Watch_Dogg
Author: Deathgod121
Date: 2021-09-19

Screen image comparison tool

Hi Everyone,

I created a small Python script that i use to compare my screen output to a predefined image and alert me once my screen or section of screen matches my configured desire. The script will watch a small section of the screen and compare that to a image array of what that small section looks like now. If the screenshot is a match we send a Push Bullet (https://www.pushbullet.com/) alert to our phone.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Prerequisites:

Python 3.6+ (https://www.python.org/downloads/)


Python Modules we pip install these (https://www.geeksforgeeks.org/how-to-install-pip-on-windows/):

pip NumPy

pip pyAutoGUI 

pip Pushbullet

pip opencv-python 

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage:

Step 1: Download all the repository files that is 3 x .py files and 1 txt file (not including the README.md).

Step 2: Open the cords.txt file and keep this open as this will be our way of adjusting the output window later.

Step 3: Run the 1_Configure.py script, with the following command from a command prompt window: python "<path_to_py_file>" "<path_to_cords.txt_file>"
        - Eg: python "C:/examples/watch_dogg/1_configure.py" "C:/examples/watch_dogg/cords.txt"
        
Step 4: You will see a small display window that will show you what the section of screen we are capturing is currently. You can adjust the values in the cords.txt file and save the file to update the output window.

Step 5: Position the output window on the section of screen you want to capture as the ideal image to match to. Once you are happy with the window size and position close the script with ctrl+c or by pressing q on the output window.

Step 6: Run the 2_Save.py script, with the following command from a command prompt window: python "<path_to_py_file>" "<path_to_cords.txt_file>"
        - Eg: python "C:/examples/watch_dogg/2_Save.py" "C:/examples/watch_dogg/cords.txt"
        
Follow the prompts this will now save the image for comparison later. A preview of the saved image will be displayed to be sure you are happy with the intended comparitor. This will create a new file at the same location as the cord.txt file with the extention "MATCH_FOUND_ARRAY_DO_NOT_REMOVE_ME.npy", plase do not remove this file.

Step 7: Create a push bullet account (https://www.pushbullet.com/) then click setup your phone and configure your phone with push bullet.

Step 8: On your computer on your push bullet account, go to settings and click create access token. Copy this token.

Step 9: Open the file 3_Watch_dogg.py with a text editor of your choice and configure the section on lines 14, 17, 20 and 23. Save the changes once you are done.

Step 8: Creating a executable file for the script this will make launching it easier. To do this create a new txt file and give it a name, watch_dogg.bat then in this file paste the following: python "<path_to_3_watch_dogg.py_file>" "<path_to_cords.txt_file>"
   - Eg: python "C:/examples/watch_dogg/3_Watch_dogg.py" "C:/examples/watch_dogg/cords.txt"

This will create a batch file that we can double click to run the script.

Step 9: Run your batch file and leave open. Whenever a match is found a alert will be sent to your phone. 




There is no error handling what so ever so please be sure to follow all steps carefully as debugging will be a nightmare...
