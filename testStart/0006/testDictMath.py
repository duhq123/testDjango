# 怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
'''
为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来

'''


def dictMath(mathNums):
    '''
        类似的，可以使用 zip() 和 sorted() 函数来排列字典数据
        执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器

        for exmaple:
            prices_and_names = zip(prices.values(), prices.keys())
            print(min(prices_and_names)) # OK
            print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
    '''
    min_mathNums = min(zip(mathNums.values(), mathNums.keys()))

    max_mathNums = max(zip(mathNums.values(), mathNums.keys()))

    mathNums_sorted = sorted(zip(mathNums.values(), mathNums.keys()))

    print(min_mathNums, max_mathNums, mathNums_sorted)

    return min_mathNums, max_mathNums, mathNums_sorted


if __name__ == '__main__':
    mathNums = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    dictMath(mathNums)
