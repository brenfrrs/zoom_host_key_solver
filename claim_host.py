import itertools
import pyautogui
import pyperclip
import logging
import time
from pynput.mouse import Button, Controller



mouse = Controller()


master_key = []

comb = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=6))

for i in comb:
    res = ''.join(str(x) for x in i)
    master_key.append(res)


nex = iter(master_key)


locate_claim = pyautogui.locateOnScreen('screen_finds/claimhostalt.png', confidence=.9)
print(locate_claim)
claim_point = pyautogui.center(locate_claim)
print(claim_point)
pyautogui.click(claim_point.x*.5, claim_point.y*.5)


def find_input():
    try:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/inputbox.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)
    except:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/grayinput.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)

find_input()

def click_claim():
    try:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/blueclaimhost.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)
    except:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/blueclaimhost.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)

# #
def turn_key(i):
        return next(i)

def copy(keycode):
    pyperclip.copy(keycode)
    print("Trying {}".format(keycode))

def paste(keycode):
    pyautogui.write(keycode)
    pyautogui.press('enter')

def find_host():
    pass

def test_code(code):
    counter = 0
    key = turn_key(code)
    copy(key)
    paste(key)
    click_claim()
    pyautogui.move(-100, 0)
    time.sleep(.5)
    mouse.click(Button.left, 2)
    pyautogui.press('backspace')
    #find_input()
    for i in range(25):
        test_code(nex)
        counter +=1
test_code(nex)
