import pyautogui
import keyboard
import time
import os 

# for i in range(20):
#     pyautogui.click(button='right')



# pyautogui.typewrite("Salam Kiria")


keyboard.press_and_release("windows+r")
time.sleep(0.5)
pyautogui.typewrite("cmd")
time.sleep(0.5)
keyboard.press_and_release("enter")
time.sleep(0.5)

code_list = ["color A", "dir"]

for command in code_list:
    pyautogui.typewrite(command)
    time.sleep(0.5)
    keyboard.press_and_release('enter')

 

link = "https://www.toplearn.com"

keyboard.press_and_release('windows+r')
time.sleep(1)
pyautogui.write(link)
time.sleep(0.3)
keyboard.press_and_release('enter')



# while True:
#     pyautogui.moveTo(100 , 100 , duration=2)
#     pyautogui.moveTo(100 , 500 , duration=2)
#     pyautogui.moveTo(500 , 500 , duration=2)
#     pyautogui.moveTo(500 , 100 , duration=2)



