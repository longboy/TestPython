# 利用正则摘取网页邮箱
from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.implicitly_wait(6)

driver.get("http://home.baidu.com/contact.html")
# 得到页面源代码
doc = driver.page_source
# 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
emails = re.findall(r'[\w]+@[\w\.-]+', doc)
# 循环打印匹配的邮箱
for email in emails:
    print(email)