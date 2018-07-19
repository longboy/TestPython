import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.baidu.com")
time.sleep(1)
# 弹框
# driver.execute_script("window.alert('这是一个alert弹框。');")
# time.sleep(2)
# driver.switch_to_alert().accept()
driver.get("https://tieba.baidu.com/index.html")
time.sleep(1)

target_elem = driver.find_element_by_link_text("人文自然")
driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
