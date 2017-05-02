from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()
driver.get("https://gabrielecirulli.github.io/2048/")

elem = driver.find_element_by_class_name("game-container")
for x in range(300):
  elem.send_keys(Keys.ARROW_DOWN)
#  time.sleep(0.1)
  elem.send_keys(Keys.ARROW_LEFT)
#  time.sleep(0.1)
  elem.send_keys(Keys.ARROW_UP)
#  time.sleep(0.1)
  elem.send_keys(Keys.ARROW_RIGHT)
#  time.sleep(0.1)
driver.close()
