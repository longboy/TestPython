from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 25)
waitPopWindow = WebDriverWait(browser, 25)

browser.get("http://haokan.baidu.com/?fr=pc_pz#doubiju")
browser.refresh()
for y in range(300):
    js = 'window.scrollBy(0,100)'
    browser.execute_script(js)
    time.sleep(0.5)

print("拖动滑动条到底部...")

browser.quit()
