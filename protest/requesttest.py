# request的get请求
import requests

url = "http://www.baidu.com/s?"
wd = input("请输入搜索内容：")
kw = {
    "wd": wd
}
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
rsp = requests.get(url=url, params=kw, headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)
