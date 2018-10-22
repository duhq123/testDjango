'''
一般来讲，代码中如果出现大量的硬编码下标会使得代码的可读性和可维护性大大降低。
比如，如果你回过来看看一年前你写的代码，你会摸着脑袋想那时候自己到底想干嘛啊。
这是一个很简单的解决方案，它让你更加清晰的表达代码的目的。

内置的 slice() 函数创建了一个切片对象。所有使用切片的地方都可以使用切片对象。
'''
import random

def testSlice(items):
    slice_beg = random.randint(0, len(items)-2)
    slice_end = random.randint(1, 1000)
    slice_step = random.randint(0, 9)
    a = slice(slice_beg, slice_end, slice_step)
    print(f'start: {a.start}, stop: {a.stop}, step: {a.step}\n',items[slice_beg:slice_end])
    return a

if __name__ == '__main__':
    items = [0, 1, 2, 3, 4, 5, 6]
    testSlice(items)