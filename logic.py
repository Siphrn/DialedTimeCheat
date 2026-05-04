import pyautogui
from pynput import keyboard
import time

POSITION_OF_CIRCLE = (900, 639)

def check_for_circle(POSITION_OF_CIRCLE):
    time_lit = 0
    while True:
        pixel_color = pyautogui.pixel(*POSITION_OF_CIRCLE)
        if pixel_color != (0, 0 ,0):  # Assuming the circle is red
            print(f"Detected for {time_lit} seconds.")
            pyautogui.click(*POSITION_OF_CIRCLE)
            time.sleep(0.1)
            time_lit += 0.1
        else:
            return time_lit
        

def replicateTime(timeLit, position):
    print(f"Replicating time: {timeLit} seconds.")
    pyautogui.mouseDown(*position)
    time.sleep(timeLit)
    pyautogui.mouseUp(*position)
    print("Done replicating time.")

