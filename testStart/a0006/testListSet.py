'''
怎样在一个序列上面保持元素顺序的同时消除重复的值？
'''


def testSetOne(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item # 生成值 item
            seen.add(item)
    return seen

def testSetTwo(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
    return seen




from collections import Counter
'''
    怎样找出一个序列中出现次数最多的元素呢？
'''
def testWordNums(words):
    word_counts = Counter(words)
    # top_three = word_counts.most_common(3)
    # print(word_counts,'\n',top_three)
    print(word_counts)
    # return top_three


'''
    你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
'''
def testListSort(testList):
    return 0



if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(testSetOne(a)))

    c = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    print(list(testSetTwo(c, key=lambda d: (d['x'],d['y']))))

    words = [
        'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
        'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
        'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
        'my', 'eyes', "you're", 'under'
    ]
    testWordNums(words)