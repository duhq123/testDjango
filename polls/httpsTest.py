# import requests
# #
# # r = requests.get('https://data.taijihuabao.com/')       # 最基本的不带参数的get请求
# # print(r.status_code)                               # 获取返回状态
# r1 = requests.get(url='http://127.0.0.1:8000/polls/', params={'key':'2'})      # 带参数的get请求
# print(r1.url)
# print(r1.text)        # 打印解码后的返回数据
#
#
# # # coding=utf-8
# # import urllib.parse
# # import urllib.request
# #
# # data = bytes(urllib.parse.urlencode({'Username': 'admin', 'Password': 'adminadmin'}), encoding='utf8')
# # response = urllib.request.urlopen('http://127.0.0.1:8000/admin/login/?next=/admin/', data=data)
# # print(response.read())

#
# import urllib.request
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='http://127.0.0.1:8000/admin/',
#                           user='admin',
#                           passwd='adminadmin')
# opener = urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# request=urllib.request.urlopen('http://127.0.0.1:8000/admin/')
# print(request.read())
# print(request.url)
# print(request.read().decode("utf8"))
# print(u'Response code:\n', request.getcode(), request.msg)
# print(u'headers:\n', request.headers)


import urllib.request
import ssl, json
import requests

# 处理HTTPS请求 SSL证书验证 忽略认证 比如12306 网站
# url = "https://www.12306.cn/mormhweb/"
url = 'https://data.taijihuabao.com/api-auth/'
header = {'Content-Type': "application/json"}
    # "Content-Type": "application/json",
    # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36"}

data = {"username": "tjhb", "password": "daochi12e"}
# data = json.dumps(data, ensure_ascii=False)
# request = urllib.request.Request(url, data=data, headers=header)
# context = ssl._create_unverified_context()
# res = urllib.request.urlopen(request, context=context)
requests.packages.urllib3.disable_warnings()
res = requests.post(url=url, json=data, headers=header, verify=False)
print(res.text)

# a=res.read().decode("utf8")
# print(a)
b=json.loads(res.text)
# print(u'Response code:\n', res.getcode(), res.msg)
#
# # print(u'Response body:\n', res.read().decode("utf8"))
# print(u'Response body:\n', a)
#
# # print(u'Response headers:\n', res.headers)
url1 = 'https://data.taijihuabao.com/api/v2/customerauth/verify_nmi/'
data1 = {"name": "杜红强", "mobile": "18231066871", "id_card": "130434199608187535"}
# res1=requests.post(url=url1,json=data1,headers=header,verify=False)
# data1 = json.dumps(data1).encode('utf-8')
print(b)
for s in b:
    if s.__eq__('token'):
        token = 'JWT ' + b[s]
        print(u'token:\n',token)
        header.setdefault('Authorization', token)
        print(header)
        res1 = requests.post(url=url1, json=data1, headers=header, verify=False)
        print(res1.text)
#         request1 = urllib.request.Request(url1, data=data1, headers=header)
#         res1 = urllib.request.urlopen(request1, context=context)
#         print(u'Response code:\n', res1.getcode(), res1.msg)
#
#         print(u'Response body:\n', res1.read().decode("utf8"))
        break
    else:
        continue
