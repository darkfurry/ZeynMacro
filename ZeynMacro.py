
import pyautogui as pag
import time
import keyboard
import sys

pag.alert('press Q once! /press B to stop /DELAY 600sec!!')
while True:
   keyboard.wait('q')
   while not keyboard.is_pressed('b'):
            keyboard.press('ctrl+v')
            pag.press('enter')
            time.sleep(600)
   pag.alert('end program')
   sys.exit()