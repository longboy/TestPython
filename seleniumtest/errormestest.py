# 错误提示判断
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
driver.implicitly_wait(3)

# 点击登录
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
# 点击用户名登录
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
error_mes = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text
try:
    assert error_mes == '请您输入手机/邮箱/用户名'
    print('Test pass.')
except Exception as e:
    print("Test fail.", format(e))
time.sleep(1)
driver.quit()
