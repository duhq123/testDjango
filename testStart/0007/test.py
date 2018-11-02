
x = 0

def test(num):
    global x
    if num ==1:
        # x = 1
        x =  test1()
        print(x)
    if num ==2:
        print(x)
        x = tets2()
    if num == 3:
        #
        print(x)
        x = 3

def test1():
    a = 1
    return a

def tets2():
    b = 2
    return b


if __name__ == '__main__':
    test(1)
    test(3)
    test(2)
    test(3)