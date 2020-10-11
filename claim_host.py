import itertools
import pynput
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import pyperclip
import logging
import time

mouse = MouseController()
keyboard = KeyboardController()
start_stop_key = KeyCode(char='s')

master_key = []

comb = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=6))

for i in comb:
    res = ''.join(str(x) for x in i)
    master_key.append(res)


nex = iter(master_key)
# #
def turn_key(i):
        return next(i)

def copy(keycode):
    pyperclip.copy(keycode)
    time.sleep(.50)
    mouse.click(Button.left, 2)
    mouse.move(0, 50)
    mouse.click(Button.left, 2)

def paste():
    keyboard.press(Key.cmd)
    time.sleep(.50)
    keyboard.press('v')
    time.sleep(.50)
    keyboard.release('v')
    keyboard.release(Key.cmd)





# print('The current pointer position is {0}'.format(mouse.position))


def test_code(code):
    counter = 0
    mouse.position = (540.77734375, 84.69140625)
    key = turn_key(code)
    copy(key)
    paste()
    for i in range(25):
        test_code(nex)
        counter +=1


test_code(nex)
