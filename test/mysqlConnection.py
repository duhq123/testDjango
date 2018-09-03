# coding=utf-8
import pymysql
import csv, os


def connectdb():
    print('连接到mysql服务器...')
    # 打开数据库连接
    # 用户名:root, 密码:123456.,用户名和密码需要改成你自己的mysql用户名和密码，data_exchange
    db = pymysql.connect("localhost", "root", "123456", "data_exchange")
    print('连接上了!')
    return db


def querydb_getCsv(db):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 查询语句
    time = '2018-08-29 '
    args = time + '%'
    sql = "select * from users_usercall where call_time like '%s'" % args

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        messageNotKonw = ['未知', '数据查询错误']
        file_name = 'test1.csv'
        target = os.path.join('/Users/edz/Desktop', file_name)
        target_header = ['id', 'name', 'mobile', 'id_card', 'result']
        with open(target, 'w+') as f1:
            writer = csv.writer(f1)
            writer.writerow(target_header)
            for row in results:
                param = eval(row[4])
                result = eval(row[5])
                a = (1 if result.__len__() == 2 else result.__len__())
                if a == 1:
                    id, name, mobile, id_card, message = get_one(result, param)
                else:
                    id, name, mobile, id_card, message = get_more(result)
                if message in messageNotKonw:
                    writer.writerow(
                        [id, name, mobile, str(id_card), message])
                else:
                    pass
        print('结束')
    except:
        print("Error: unable to fecth data")
    finally:
        # 提交事物并关闭数据库连接
        cursor.close()
        db.commit()
        db.close()


def get_one(result, param):
    id = 0
    name = param['name']
    mobile = param['mobile']
    id_card = param['id_card']
    message = result['message']
    return id, name, mobile, id_card, message


def get_more(result):
    for i in range(int(result.__len__())):
        id = result[i]['id']
        name = result[i]['name']
        mobile = result[i]['mobile']
        id_card = result[i]['id_card']
        message = result[i]['message']
    return id, name, mobile, id_card, message


def main():
    print('开始连接数据库')
    db = connectdb()  # 连接MySQL数据库
    querydb_getCsv(db)  # 查询数据库



if __name__ == '__main__':
    main()
