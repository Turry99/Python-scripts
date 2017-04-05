from PIL import ImageGrab
import pyautogui
import time
time.sleep(5)
for x in range(1,290):
    pyautogui.click()
    time.sleep(2)
    ImageGrab.grab().save( str(x) +".jpg", "JPEG")
