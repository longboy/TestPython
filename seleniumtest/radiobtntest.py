from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.implicitly_wait(5)

for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):
    i.click()
time.sleep(3)
driver.quit()
