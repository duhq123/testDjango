import csv
import xlwt

import pandas as pd


def csv_to_xlsx():
    with open('/Users/edz/Desktop/order.csv', 'r', encoding='utf-8') as f:
        read = csv.reader(f)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('data')  # 创建一个sheet表格
        l = 0
        for line in read:
            print(line)
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)  # 一个一个将单元格数据写入
                r = r + 1
            l = l + 1

        workbook.save('1.xlsx')  # 保存Excel






def csv_to_xlsx_pd():
    csv = pd.read_csv('/Users/edz/Desktop/order.csv', encoding='utf-8')
    csv.to_excel('1.xlsx', sheet_name='data')



if __name__ == '__main__':
    # csv_to_xlsx()
    csv_to_xlsx_pd()
