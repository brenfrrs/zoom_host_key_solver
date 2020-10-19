# Zoom Claim Host Key Solver

The article describing the code for this repo can be found [here](https://medium.com/@brendanfrrs/scraping-amazon-results-with-selenium-and-python-547fc6be8bfa "Medium.com article.").

## Requirements:
To run this program you will need the following installed on your computer or virtual machine:

1. [pynput](https://pypi.org/project/pynput/)
2. [pyautogui](https://pyautogui.readthedocs.io/en/latest/)
3. [pyperclip](https://pypi.org/project/pyperclip/)

In order for the program to work properly, you need to be in a Zoom room with 'claim host' button displayed (by clicking participants). You can cancel the program at any time by typing control-c, or moving your mouse cursor to the upper left hand of your screen/monitor.

Depending on your screen resolution, you may need to remove '*.5' in the coordinates located on lines: 66, 73, 76, 89, and 92.

This script is for educational purposes and was created as a way to learn the fundamentals of pyautogui. 
