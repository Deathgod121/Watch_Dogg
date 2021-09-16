# Watch_Dogg
FFXIV Duty finder alert script

Hi Everyone,

I created a small Python script that i use to alert me when my duty finder pops. The script will watch a small section of the screen and compare that to a image array of what that small section looks like when the duty finder alert is there compared to now. If the screenshot is a match we send a Push Bullet (https://www.pushbullet.com/) alert to our phone.


Prerequisites:

Python 3.6+ (I think at least can try your luck!)
pip NumPy
pip pyAutoGUI 
pip Pushbullet


First run configuration:
