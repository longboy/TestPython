from urllib import request

if __name__ == '__main__':
    url = "http://jobs.zhaopin.com/569083721250626.htm?ssidkey=y&ss=201&ff=03&sg=e8032a4fbf00448caa38009fb9bf5807&so=1&uid=691045461"
    # 打开相应url返回相应页面
    rsp = request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("该页面url:{0}".format(rsp.geturl()))
    print("该页面info:{0}".format(rsp.info()))
    print("返回code:{0}".format(rsp.getcode()))

    html = rsp.read()
    # 解码，把byte转成字符串
    html = html.decode()
    # print(html)
