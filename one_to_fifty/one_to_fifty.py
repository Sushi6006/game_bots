# game_bot for 1to50
# completed by Sushi6006 on 28 Oct. 2019
# code available at https://github.com/Sushi6006/game_bots/blob/master/one_to_fifty/one_to_fifty.py

# a chinese online game that requires you to click 1 to 50 sequentially
# link to the game: http://wap.jue-huo.com/app/html/game/1to50/1to50.html
# Developed in Python 3.7 (anaconda) with Selenium in Atom

# xpath cheat sheet: https://devhints.io/xpath
# chrome driver download: https://chromedriver.storage.googleapis.com/index.html

# chinese tutorial: https://mp.weixin.qq.com/s?__biz=MzU2NTgyOTc0Ng==&mid=2247483672&idx=1&sn=4c9a98ede1121d8e2d5b10b3f38e6264&chksm=fcb48805cbc301136ba09245c9a2632a2735003cbb1cffcebf8ca3350a5fc1bb13a5230d4e71

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://wap.jue-huo.com/app/html/game/1to50/1to50.html")
for i in range(1, 51):
    driver.find_element_by_xpath("//*[@style=\"opacity: 1;\" and text() = '{}']".format(i)).click()
    sleep(0.05)  # removing this may make the program run faster, but the 26th div might not be loaded yet, which will make my code crash
