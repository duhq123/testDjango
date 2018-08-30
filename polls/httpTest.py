# import http.client
#
# url = 'http://127.0.0.1:8000/polls'
# conn = http.client.HTTPSConnection('127.0.0.1','8000')
# conn.request(method='POST',url=url)
#
# response = conn.getresponse()
# res = response.read()
# print(res)

# 可行
# import requests
#
# url = 'http://127.0.0.1:8000/polls'
# r = requests.get(url,'1')
# print(r.content)


# NO
# import urllib,urllib.request, urllib.error
#
# test_data = {'ClientRequest': 'aaaa', 'b': 'bbbbb'}
# test_data_urlencode = urllib.urlencode(test_data)
# # requrl = "http://baidu.com"
# requrl = "http://127.0.0.1/test.py"
#
# req = urllib.request(url=requrl, data=test_data_urlencode)
# print(req)
#
# res_data = urllib2.urlopen(req)
# res = res_data.read()
# print(res)

# 可行
# import urllib.request,urllib.response
#
# response = urllib.request.urlopen('http://127.0.0.1:8000/hello',timeout=10)
# print(response.read())

# import sys
# import BaseHTTPServer
# from SimpleHTTPServer import SimpleHTTPRequestHandler
#
# HandlerClass = SimpleHTTPRequestHandler
# ServerClass = BaseHTTPServer.HTTPServer
# Protocol = "HTTP/1.0"
#
# if sys.argv[1:]:
#     port = int(sys.argv[1])
# else:
#     port = 8000
# server_address = ('127.0.0.1', port)
#
# HandlerClass.protocol_version = Protocol
# httpd = ServerClass(server_address, HandlerClass)
#
# sa = httpd.socket.getsockname()
# print
# "Serving HTTP on", sa[0], "port", sa[1], "..."
# httpd.serve_forever()


# import requests
#
# print(requests.get('http://127.0.0.1:8000/hello').text)
# print()
#
# import urllib.request
#
# r = urllib.request.urlopen('https://www.baidu.com/')
# print(r)
# #
# import urllib
# import urllib.request, urllib.response, urllib.error
#
#
# def get_Http():
#     try:
#         r = urllib.request.urlopen('http://www.baidu.com')
#         print(u'Response code:\n', r.getcode(), r.msg)
#         print(u'headers:\n', r.headers)
#     except urllib.error.URLError:
#         print('url错误')
#     except ConnectionRefusedError:
#         print('连接失败')
#
#
# get_Http()

import urllib.request, urllib.parse
import ssl, json

# 处理HTTPS请求 SSL证书验证 忽略认证 比如12306 网站
# url = "https://www.12306.cn/mormhweb/"
url = 'http://127.0.0.1:8000/hello'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
# data = {
#     'password': 'daochi12e',
#     'username': 'tjhb'
# }
# data = json.dumps(data).encode('utf-8')
# print(data)
try:
    request = urllib.request.Request(url, headers=header)
    # res = urllib.request.urlopen(request)
    context = ssl._create_unverified_context()
    # ssl._create_default_https_context = ssl._create_unverified_context
    res = urllib.request.urlopen(request, context=context)

    print(res.read().decode("utf8"))
    print(u'Response code:\n', res.getcode(), res.msg)
    print(u'headers:\n', res.headers)

except urllib.error.URLError:
    print('URL错误')
except ConnectionError:
    print('连接失败')
