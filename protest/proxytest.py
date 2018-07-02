# 使用代理访问百度网站
# 推荐一个官网，最新代理ip http://www.goubanjia.com
from urllib import request, error

if __name__ == '__main__':
    url = "http://www.baidu.com"
    # 设置代理地址
    proxy = {'http': '39.137.77.66:8080'}
    # 创建proxyhandler
    proxy_handler = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxy_handler)
    # 安装opener
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
