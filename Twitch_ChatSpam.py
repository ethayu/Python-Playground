#Get that Valorant Beta Key bois
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(15)
x = 65

while True:
    if (x == 123): x = 65
    keyboard.press(chr(x))
    keyboard.release(chr(x))
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    x = x + 1
    sec = 180
    while sec != 0:
        sec-= 1
        time.sleep(1)