import random
import string

import time
import requests
from py_aiplat_py3 import apiutil

class robotchat:
    def __init__(self):
        self.app_id = '2109911818'
        self.app_key = 'Gxti0kDMDeaT8kzm'
        self.url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'

    def chat(self, session, question):
        params = {}
        params['app_id'] = int(self.app_id)
        params['app_key'] = self.app_key
        params['time_stamp'] = int(time.time())
        params['nonce_str'] = ''.join(random.sample(string.digits, 8))

        params['session'] = session
        params['question'] = question
        sign = apiutil.genSignString(params)
        params['sign'] = sign

        return params

    def getwords(self, params):
        res = requests.post(self.url, params)
        return res.json()

if __name__ == '__main__':
    rb = robotchat()
    a = 0
    flage = True
    while True:
        # if a == 0 :
        #     session = input('--Please input your session?\n--')
        #     a +=1
        session = random.randrange(1, 99999)
        # print(session)
        question = input('--Please input your question?\n--')
        params = rb.chat(session, question)
        res_data = rb.getwords(params)
        while flage:
            if res_data !='':
                print(f"--robot answer:\n--{res_data['data']['answer']}")
                break
            else:
                flage = True