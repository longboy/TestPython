import time
import unittest
from selenium import webdriver


class UnitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(6)
        self.driver.get("http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_search_baidu(self):
        self.driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(1)
        self.driver.find_element_by_id("su").click()
        time.sleep(1)
        try:
            assert 'selenium' in self.driver.title
            print("Test pass")
        except Exception as e:
            print('Test fail', format(e))


if __name__ == '__main__':
    unittest.main()
