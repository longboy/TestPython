from urllib import request, parse
# 分析百度词典
# 负责处理json格式的模块
import json

baseurl = 'http://fanyi.baidu.com/sug'
kw = input("请输入要查询的单词：")
data = {
    # girl应该是输入
    'kw': kw
}

data = parse.urlencode(data).encode("utf-8")
headers = {
    'Content-Length': len(data)
}

req = request.Request(url=baseurl, data=data, headers=headers)
rsp = request.urlopen(req)
json_data = rsp.read().decode("utf-8")
print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'], item['v'])
