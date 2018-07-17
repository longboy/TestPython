# 利用火狐浏览器选择菜单打开图片
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.baidu.com')
time.sleep(2)

element = driver.find_element_by_xpath("//*[@id='lg']/img[2]")
actionChains = ActionChains(driver)
actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
