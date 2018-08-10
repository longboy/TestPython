# 测试logger类
import time
from  selenium import webdriver
from seleniumtest.loggertest import Logeer

mylogger = Logeer(logger='Testlog').getlog()


class Testlog(object):
    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.info("打开浏览器")
        driver.maximize_window()
        mylogger.info("最大化浏览器窗口。")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        mylogger.info("打开百度首页。")
        time.sleep(1)
        mylogger.info("暂停一秒。")
        driver.quit()
        mylogger.info("关闭并退出浏览器。")


testlog = Testlog()
testlog.print_log()
