# 切换单选框 判断是否选中了单选框
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://news.baidu.com')
driver.implicitly_wait(5)

for i in driver.find_elements_by_xpath("//*/input[@type='radio']"):
    i.click()
time.sleep(3)
try:
    assert driver.find_element_by_xpath("//*[@id='news']").is_selected() == True
    print('Test Pass.')
except Exception as e:
    print('Test fail', format(e))

driver.quit()
