# -*- coding: utf-8 -*-

import os
import json
from testStart.a0004.a0004 import get_word_frequencies


def Test1(rootDir):
    list_dirs = os.walk(rootDir)

    for root, dirs, files in list_dirs:
        for d in dirs:
            print('文件夹' + os.path.join(root, d))
        for f in files:
            print('文件' + os.path.join(root, f))


def Test2(rootDir):
    for lists in os.listdir(rootDir):

        path = os.path.join(rootDir, lists)


        # print(path)
        filename = os.path.basename(path)
        # print(filename)
        # print(os.path.splitext(filename)[0])
        # print(os.path.splitext(filename)[-1])
        # print(os.path.splitext(filename)[-1][1:])
        filename_end = os.path.splitext(filename)[-1]
        # print(filename_end)
        if filename_end == '.txt':
            #  判断文件后缀，然后读取文件
            print(path)
            try:
                dic = get_word_frequencies(path)
                max_times = 0
                max_name = ''
                for i, k in dic.items():
                    max_name, max_times =(i, k) if k >= max_times  else (max_name, max_times)
                print(f'url: {os.path.abspath(os.path.dirname(path))}, fileName: {os.path.basename(path)}, max_name: {max_name}, max_times: {max_times}')
            except Exception as e:
                print(e)
                continue

        if os.path.isdir(path):
            Test2(path)


if __name__ == '__main__':
    path = '/Users/edz/Desktop'
    # Test1(path)
    Test2(path)
