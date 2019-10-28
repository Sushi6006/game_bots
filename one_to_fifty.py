# game_bot for 1to50
# a chinese online game that requires you to click 1 to 50 sequentially
# link: http://wap.jue-huo.com/app/html/game/1to50/1to50.html

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://wap.jue-huo.com/app/html/game/1to50/1to50.html")
for i in range(1, 51):
    driver.find_element_by_xpath("//*[@style=\"opacity: 1;\" and text() = '{}']".format(i)).click()
    sleep(0.05)  # removing this may make the program run faster, but the 26th div might not be loaded yet, which will make my code crash
