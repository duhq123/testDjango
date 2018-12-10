def testDictCompare(a, b):
    print(a.keys() & b.keys())
    print(a.keys() | b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())
    '''
        假如你想以现有字典构造一个排除几个指定键的新字典。
    '''
    print({key:a[key] for key in a.keys() - {'z', 'w'}})

if __name__ == '__main__':
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }
    testDictCompare(a, b )