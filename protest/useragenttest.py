from urllib import request, parse

# 使用用户代理
if __name__ == '__main__':
    url = "http://www.baidu.com"

    try:
        headers = {}

        headers[
            "User-Agent"] = 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'

        req = request.Request(url, headers=headers)
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except Exception as e:
        print(e)
