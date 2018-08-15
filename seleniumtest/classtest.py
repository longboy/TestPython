import time
from selenium import webdriver
'''
父类
'''

class ClassTest(object):
    def open_baidu(self):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()
        driver.implicitly_wait(6)
        time.sleep(1)
        print('即将退出')
        driver.quit()
        print('已经退出')
