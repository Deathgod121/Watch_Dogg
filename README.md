# Watch_Dogg
FFXIV Duty finder alert script

Hi Everyone,

I created a small Python script that i use to alert me when my duty finder pops. The script will watch a small section of the screen and compare that to a image array of what that small section looks like when the duty finder alert is there compared to now. If the screenshot is a match we send a Push Bullet (https://www.pushbullet.com/) alert to our phone.


Prerequisites:

Python 3.6+ (I think at least can try your luck!)

pip NumPy

pip pyAutoGUI 

pip Pushbullet




First run the configuration_scipt:

Please read the code comments and follow the step to configure there.




Once configured:

Create a batch file to run your script. Open a text Editor and paste the contents below into it (remember to replace tokens). Save file as <file_name>.bat:

"<OPTIONAL* path to python.exe>" "<path to script file>/watch_dogg.py"
  
 
EG: "C:/Program Files/Python39/python.exe" "e:/pyth/projects/ffxiv/watch_dogg.py"
  
  
* Note the path is optional incase you dont have the environment variable defined. Otherwise python <path> is fine.
  
  

  
To start the script just double click the bat file. To stop simply close the window.
