# 摘取所有图片信息
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("http://news.baidu.com")

time.sleep(3)
# 图片信息
# for image in driver.find_elements_by_tag_name("img"):
#     print(image.size)
# href元素
for link in driver.find_elements_by_xpath("//*[@href]"):
    print(link.get_attribute('href'))

driver.quit()
