import time,sys, pyautogui

width, height = pyautogui.size() #gets us screen resolution
pyautogui.PAUSE = 0.05           #after each function call, wait this many seconds


#after a 5 second delay, press keys super fast in the order "g, a, t, f" and enter
#repeat over and over

#
#

startupdelay = 3   #how long to wait after starting program
#main program runs here:


print("Going")
time.sleep(startupdelay)
print("Ready to go!")

counter = 0
while counter < 200:
    pyautogui.typewrite(['g','a','t','f','enter'], 0.05) #types the letters 'gatf', 0.25 second delay between each
    
    if counter%10 == 0: #tells you how many times its done it every 10 times
        print(counter)
    counter += 1