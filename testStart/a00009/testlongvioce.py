import base64
import csv
import fnmatch
import hashlib
import os
import random
import string

import time
import requests
from pandas import json
from py_aiplat_py3 import apiutil
from tjtts.VoiceUtils import wav_8k_to_16k
from tjtts.aiqqasrapi import AiQQAsrApi
from pydub.generators import AudioSegment

import json
from aip import AipSpeech




# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()




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
    params['callback_url'] = 'http://ttsoa.tjhb.info/api/v1/voicefile/long_voice_callback/'
    params['speech'] = speech

    sign = apiutil.genSignString(params)
    params['sign'] = sign

    url = 'https://api.ai.qq.com/fcgi-bin/aai/aai_wxasrlong'
    print(params)
    res = requests.post(url, params)
    print(res.text)

    return res.text


def call_back():
    params = {}
    params['ret'] = 0
    params['msg'] = 'ok'
    params['data'] = {
        "task_id": "615168_1543212626420",
        "text": "result_text",
    }
    url = 'http://ttsoa.tjhb.info/api/v1/voicefile/long_voice_callback/'
    ret = requests.post(url, params)
    return ret





if __name__ == '__main__':
    # call()
    # print(call_back().text)

    APP_ID = '15096059'
    API_KEY = 'su22cNBI6PcTfEXwE3ObwoM7'
    SECRET_KEY = 'HEsLQq4nrYiZHA2litIQ9YW2IEzeasjM'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


    dirname = '/Users/edz/Desktop/2222222'
    #
    file_name = 'test3.csv'
    target = os.path.join('/Users/edz/Desktop', file_name)
    target_header = ['file_path', 'code', 'data']
    with open(target, 'w+') as f1:
        writer = csv.writer(f1)
        writer.writerow(target_header)
        files = os.listdir(dirname)
        files.sort()
        for file in files:
            print(file)
            if fnmatch.fnmatch(file, '*.wav'):
                path = os.path.join(dirname, file)
                print(path)
                wav_8k_to_16k(path)
                data = ''
                try:
                    # 识别本地文件
                    res = client.asr(get_file_content(path), 'wav', 16000, {
                        'dev_pid': 1537,
                    })

                    code = res['err_no']
                    err_msg = res['err_msg']
                    result = res['result']

                    print(code, err_msg)

                    if code == 0:
                        print(result)
                        data = result
                    # code, data = wav_file_proccess2(path)
                except Exception as e:
                    print(e)
                    code, data = -1, ''
                writer.writerow([path, code, data])











