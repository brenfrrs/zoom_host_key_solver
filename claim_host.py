import itertools
import pyautogui
import pyperclip
import logging
import time
import timeit
import random
from pynput.mouse import Button, Controller

start = time.time()

pyautogui.FAILSAFE = True

mouse = Controller()


master_key = [] #master list of combinations


# each comb is a list of all n digit numbers based on 'repeat' value.

comb6 = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=6))
#comb7 = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=7))
#comb8 = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=8))
#comb9 = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=9))
#comb10 = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=10))

final_list = comb6 #+ comb7 + comb8 + comb9 + comb10
random.shuffle(final_list)

print(final_list[:10])

for i in final_list:
    #each number is a list of digits, this function joins
    #each number list to create a list of numbers, then
    #appends the number into the master_key list.
    res = ''.join(str(x) for x in i)
    master_key.append(res)


nex = iter(master_key) # turn master list into an iterator so we can grab
                       # one number at a time.


locate_claim = pyautogui.locateOnScreen('screen_finds/claimhostalt.png', confidence=.9)
print(locate_claim)
claim_point = pyautogui.center(locate_claim)
print(claim_point)
pyautogui.click(claim_point.x*.5, claim_point.y*.5)

time.sleep(.2)

def find_input():
    '''
    Find the input box from the claim host popup.
    '''
    try:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/inputbox.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)
    except:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/grayinput.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)

find_input()

def click_claim():
    '''
    Click the blue claim host button that appears after
    numbers are entered.
    '''
    try:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/blueclaimhost.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)
    except:
        input_box_x, input_box_y = pyautogui.locateCenterOnScreen('screen_finds/blueclaimhost.png', confidence=.9)
        pyautogui.click(input_box_x*.5, input_box_y*.5)

# #
def turn_key(i):
    '''
    Grab the next number from the master_list
    '''
        return next(i)

def copy(keycode):
    pyperclip.copy(keycode)
    print("Trying {}".format(keycode))

def paste(keycode):
    pyautogui.write(keycode)
    pyautogui.press('enter')

def test_code(code):
    key = turn_key(code)
    copy(key)
    paste(key)
    click_claim()
    pyautogui.move(-100, 0)
    mouse.click(Button.left, 2)
    pyautogui.press('backspace')
    end = time.time()
    for i in range(25):
        test_code(nex)

test_code(nex)
