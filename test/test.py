# -*- coding:utf-8 -*-
__author__ = 'zhuyuru'
#参考 https://www.jianshu.com/p/4e39444d5ebc
# from workbook import Workbook
import os
import sys
import time
# pip install xlwt
import xlwt

list = []


def parsefile(filepath, mark):
    print("[info]============>parse_file")
    dic = {}
    try:
        begin = time.time()
        [des_filename, extname] = os.path.splitext(filepath)
        nfilename = des_filename + '_' + str("r") + extname
        # 处错误 就改成gb18030
        f_read = open(filepath, encoding='UTF-8')
        # 具体处理
        rownum = 0
        for eachline in f_read:
            splitarr = eachline.split(mark)
            list.append(splitarr)
            rownum = rownum + 1
            if (rownum % 10000 == 0):
                print("[info]parse_file %s" % (rownum))
    except:
        print(sys.exc_info()[0], sys.exc_info()[1])
    finally:
        f_read.close()
        end = time.time()
        print("[info]======>format file %s  ,spend time %d s" % (filepath, (end - begin)))
        return dic;


def create_xls(file_path, list):
    workbook = xlwt.Workbook(encoding = 'utf-8')  # 注意Workbook的开头W要大写
    sheet1 = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    # 向sheet页中写入数据
    for i, j in enumerate(list):
        if (i % 10000 == 0):
            print("执行到第%s行" % (i + 1))
        for s, k in enumerate(j):
            sheet1.write(i, s, str(k))
    file_path = file_path.replace('\\', '/')
    workbook.save(file_path)
    print('创建excel文件完成！')
    return file_path


if __name__ == '__main__':
    srcfile = '/Users/edz/Desktop/order.csv'
    floder = os.path.dirname(os.path.realpath(__file__))
    # srcfile=floder+u'/srcdata.csv'
    print("srcfile:%s"%(srcfile))
    [des_filename, extname] = os.path.splitext(srcfile)
    parsefile(srcfile, ',')#解析文件
    create_xls(des_filename + u"_r.xls", list)#将解析后的文件输出到excel
