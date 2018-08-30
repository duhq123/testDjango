import requests,json,random,datetime

def execute():
    requests.packages.urllib3.disable_warnings()
    login_url = 'https://data.taijihuabao.com/api-auth/'
    login_header = {"Content-Type": "application/json"}
    # "User-Agent": "Mozilla/5.0 (Mcintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
    login_data = {"username": "tjhb", "password": "daochi12e"}
    # login_data = json.dumps(login_data).encode('utf-8')

    try:
        # login_request = urllib.request.Request(login_url, data=login_data, headers=login_header)
        # context = ssl._create_unverified_context()
        # login_response = urllib.request.urlopen(login_request, context=context)
        login_response = requests.post(url=login_url, json=login_data, headers=login_header, verify=False)
        login_response_code = login_response.status_code
        login_response_body = login_response.text
        print(u'登陆返回响应结果:\n', login_response_code, login_response.ok)
        if login_response_code.__eq__('200'):

            # print(u'Response body:\n', login_response_body)
            # 将返回结果转换为json格式
            login_response_body = json.loads(login_response_body)
            # print(u'Response headers:\n', res.headers)

            # print(post_data)
            for is_token in login_response_body:
                if is_token.__eq__('token'):
                    post_header_token = 'JWT ' + login_response_body[is_token]
                    print(u'token:\n', post_header_token)
                    login_header.setdefault('Authorization', post_header_token)
                    post_url = 'https://data.taijihuabao.com/api/v2/customerauth/verify_nmi/'
                    mobile='1823106'+str(random.randint(1000,9999))
                    post_data = {"name": "杜红强", "mobile": "", "id_card": "130434199608187535"}
                    post_data.__setitem__('mobile', mobile)
                    # post_data = json.dumps(post_data).encode('utf-8')
                    print(login_header)
                    try:
                        # post_request = urllib.request.Request(post_url, data=post_data, headers=login_header)
                        # post_response = urllib.request.urlopen(post_request, context=context)
                        post_response = requests.post(url=post_url, json=post_data, headers=login_header, verify=False)
                        print(u'Response code:\n', post_response.status_code,post_response.ok)
                        #
                        print(u'Response body:\n', post_response.text)
                        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 现在
                        print('系统测试成功，当前时间为：', nowTime)
                        break
                    except requests.RequestException:
                        print('URL错误')
                        return 'ok'
                else:
                    continue
        else:
            return 'ok'
    except requests.RequestException:
        print('URL错误')
        return 'ok'
    except ConnectionError:
        print('连接失败')
        return 'ok'


if __name__ == '__main__':
    execute()

# # 处理HTTPS请求 SSL证书验证 忽略认证
# login_url = 'https://data.taijihuabao.com/api-auth/'
# post_url = 'https://data.taijihuabao.com/api/v2/customerauth/verify_nmi/'
# login_header = {
#     "Content-Type": "application/json",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"}
#
# login_data = {"username": "tjhb", "password": "daochi12e"}
# login_data = json.dumps(login_data).encode('utf-8')
# post_data = {"name": "杜红强", "mobile": "18231066872", "id_card": "130434199608187535"}
# post_data = json.dumps(post_data).encode('utf-8')
# try:
#     login_request = urllib.request.Request(login_url, data=login_data, headers=login_header)
#     context = ssl._create_unverified_context()
#     login_response = urllib.request.urlopen(login_request, context=context)
#
#     login_response_code = login_response.getcode()
#     login_response_body = login_response.read().decode("utf8")
#     # print(a)
#
#     print(u'登陆返回响应结果:\n', login_response_code, login_response.msg)
#     if login_response_code.__eq__('200'):
#
#         # print(u'Response body:\n', login_response_body)
#         # 将返回结果转换为json格式
#         login_response_body = json.loads(login_response_body)
#         # print(u'Response headers:\n', res.headers)
#
#         # print(post_data)
#         for is_token in login_response_body:
#             if is_token.__eq__('token'):
#                 post_header_token = 'JWT ' + login_response_body[is_token]
#                 # print(u'token:\n', post_header_token)
#                 post_header = login_header.setdefault('Authorization', post_header_token)
#                 # print(post_header)
#                 post_request = urllib.request.Request(post_url, data=post_data, headers=post_header)
#                 post_response = urllib.request.urlopen(post_request, context=context)
#                 print(u'Response code:\n', post_response.getcode(), post_response.msg)
#
#                 print(u'Response body:\n', post_response.read().decode("utf8"))
#                 break
#             else:
#                 continue
#     else:
#         breakpoint()
# except urllib.request.URLError:
#     print('URL错误')
# except ConnectionError:
#     print('连接失败')
