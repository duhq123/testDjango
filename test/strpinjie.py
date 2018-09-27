import  json, datetime

def testJson():
    print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
    a = ''
    print(a is '')
    date = '2018年8月'
    new_date = date[:4] + '-' + date[5:6] + '-1'
    print(datetime.datetime.strptime(new_date, '%Y-%m-%d').date() )

if __name__ == '__main__':
    testJson()