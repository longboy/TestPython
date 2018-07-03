from urllib import request, parse
from http import cookiejar

# 创建cookiejar的案例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    url = "https://passport.csdn.net/account/login"

    data = {
        "username": "***用户名***",
        "password": "***密码***"
    }
    # 数据编码
    data = parse.urlencode(data)
    # 创建请求对象
    req = request.Request(url, data=data.encode())
    # 使用opener发起请求
    rsp =opener.open(req)


def getHomePage():
    url = "https://my.csdn.net/ywj_486"
    # 如果已经执行了login函数，则opener自动已经包含对应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open("cookie.html", "w")as f:
        f.write(html)


if __name__ == '__main__':
    login()
    # getHomePage()

    print(cookie)