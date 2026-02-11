import random

import pyautogui as pg # type: ignore

import time
message = ("HAPPY BIRTHDAY BHAI",)

time.sleep(8)

for i in range(18):
    a=random.choice(message)
    pg.write(a)
    pg.press('enter')
    time.sleep(1.5)

