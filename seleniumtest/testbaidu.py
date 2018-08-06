from selenium import webdriver
import time
from seleniumtest.baidu_search import Baidutest


class Test(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    baidu1 = Baidutest(driver)

    def open_url(self):
        self.baidu1.get_url("http://www.baidu.com")
        time.sleep(1)

    def self_test(self):
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        try:
            assert 'selenium' in self.driver.title
            print('Test pass.')

        except Exception as e:
            print('Test fail.')
        time.sleep(1)
        self.baidu1.back()
        time.sleep(1)
        self.baidu1.forward()
        time.sleep(1)

        self.baidu1.quit_brower()


test = Test()
test.open_url()
test.self_test()
