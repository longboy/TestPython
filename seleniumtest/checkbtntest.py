# 复选框自动选择
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com')
driver.implicitly_wait(3)

# 点击登录
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
# 点击用户名登录
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
time.sleep(1)
# 点击下次自动登录
driver.find_element_by_xpath("//*[@name='memberPass']").click()
time.sleep(1)
# 同上
driver.find_element_by_xpath("//*[@name='memberPass']").click()
time.sleep(1)
driver.quit()
