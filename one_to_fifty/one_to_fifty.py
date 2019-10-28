# game_bot for 1to50
# completed by Sushi6006 on 28 Oct. 2019
# code available at https://github.com/Sushi6006/game_bots/blob/master/one_to_fifty.py

# a chinese online game that requires you to click 1 to 50 sequentially
# link to the game: http://wap.jue-huo.com/app/html/game/1to50/1to50.html
# Developed in Python 3.7 (anaconda) with Selenium in Atom

# xpath cheat sheet: https://devhints.io/xpath
# chrome driver download: https://chromedriver.storage.googleapis.com/index.html

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://wap.jue-huo.com/app/html/game/1to50/1to50.html")
for i in range(1, 51):
    driver.find_element_by_xpath("//*[@style=\"opacity: 1;\" and text() = '{}']".format(i)).click()
    sleep(0.05)  # removing this may make the program run faster, but the 26th div might not be loaded yet, which will make my code crash
