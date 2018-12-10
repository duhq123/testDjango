import base64
import random
import string

import requests
import time
from py_aiplat_py3 import apiutil


def call():
    app_id = '2109911818'
    app_key = 'Gxti0kDMDeaT8kzm'

    file_path = '/Users/edz/Desktop/update.wav'
    f = open(file_path, 'rb')
    speech = base64.b64encode(f.read()).decode()
    f.close()
    params = {}

    params['app_id'] = int(app_id)
    params['app_key'] = app_key
    params['time_stamp'] = int(time.time())
    params['nonce_str'] = ''.join(random.sample(string.digits, 8))

    params['format'] = 2
    # params['callback_url'] = 'http://sgate.taijihuabao.com/web/callback/wxasrlong/'
    params['callback_url'] = 'http://ttsoa.tjhb.info/api/v1/voicefile/long_voice_callback/'
    params['speech'] = speech

    sign = apiutil.genSignString(params)
    params['sign'] = sign

    url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_wxasrlong'
    print(params)
    res = requests.post(url, params)
    print(res.text)

    return res.text



if __name__ == '__main__':
    call()