# import csv
# import json
# import sys
# import collections # 有序字典
#
# def trans(path):
#     jsonData=open(path+'.json')
#     #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行
#     # csvfile = open(path+'.csv', 'wb')#python2下
#     csvfile = open(path+'.csv', 'w',newline='')#python3下
#     for line in jsonData:#获取属性列表
#         dic=json.loads(line[0:])
#         keys=dic.keys()
#         break
#     writer = csv.writer(csvfile)
#     writer.writerow(keys)#将属性列表写入csv中
#     for dic in jsonData:#读取json数据的每一行，将values数据一次一行的写入csv中
#         dic=json.loads(dic[0:])
#         writer.writerow(dic.values())
#     jsonData.close()
#     csvfile.close()
# # trans("test")
#
# if __name__ == '__main__':
#     trans('/Users/edz/Desktop/test')

import csv
import json
import sys
import collections # 有序字典

def trans(path):
    jsonData=open(path+'.json')
    #csvfile = open(path+'.csv', 'w')#此处这样写会导致写出来的文件会有空行
    # csvfile = open(path+'.csv', 'wb')#python2下
    csvfile = open(path+'.csv', 'w',newline='')#python3下
    data = {}
    keys_write = True
    writer = csv.writer(csvfile)

    for line in jsonData:#获取属性列表
        dic=json.loads(line[0:-1])
        keys=dic.keys()
        break

    for dic in jsonData:#读取json数据的每一行，将values数据一次一行的写入csv中

        print(dic)
        dic=json.loads(dic[0:])

        for key in keys:
            if key in dic: # has_key 已经被淘汰，使用in更加灵活
                data[key] = dic[key]
            else:
                data[key] = ""
        print(data)

        if keys_write == True:
            writer.writerow(data.keys())
        writer.writerow(data.values())
        keys_write = False

    jsonData.close()
    csvfile.close()
# trans("./dic_test")

if __name__ == '__main__':
    trans('/Users/edz/Desktop/test')