# css选择器 beautifulsoup
from urllib import request
from bs4 import BeautifulSoup

url = "http://baidu.com"
rsp = request.urlopen(url)
content = rsp.read()
soup = BeautifulSoup(content, "lxml")
content = soup.prettify()
print(content)
