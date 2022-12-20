import pyautogui
import time
import random

while(True):
	x = random.randint(0, 500)
	y = random.randint(0, 500)

	pyautogui.moveTo(x, y)

	time.sleep(3)