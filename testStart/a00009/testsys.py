import sys


def main():
    """
     通过sys模块来识别参数demo, http://blog.csdn.net/ouyang_peng/
    """
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    print('脚本名为：', sys.argv[0])
    for i in range(1, len(sys.argv)):
        print('参数 %s 为：%s' % (i, sys.argv[i]))


# hello.py
# 这是老早写的。不过今天加入了Pickle，然后润色了一下。
# 可能有点无聊（不推荐使用）

import pickle
import os.path


def search(x, data):
    for k, d in enumerate(data):
        if x == d['name']:
            return k, d


def save_data(A, pklname):
    with open(pklname, 'wb') as pkl:
        pickle.dump(A, pkl)


def load_data(pklname):
    with open(pklname, 'rb') as pkl:
        return pickle.load(pkl)


# communicating with computer
data = [] if not os.path.isfile('data') else load_data('data')



if __name__ == "__main__":
    # from functools import partial
    #
    # #
    # inputNew = partial(input, 'please input your words:\n')
    # # main()
    # sentinel = 'end'  # 遇到这个就结束
    # lines = []
    # for line in iter(inputNew, sentinel):
    #     lines.append(line)
    # print(lines)

    while True:
        print('Welcome! [type "quit" if you want to quit.]')
        name = input('--What is your name?\n--')
        if name in {'quit', 'Quit', 'q', 'Q'}:
            print('[You quit]')
            break
        if not search(name, data):
            print('--Welcome, ' + name + '. I will remember you name.')
            d = {'name': name, 'age': 0, 'history': []}
            data.append(d)
        else:
            print('--Hi, ' + name + '. How I miss you.')

        k, d = search(name, data)
        while d['age'] == 0:
            age = input('--How old are you?[I will repeat until you respond!]')
            try:
                if int(age) == 0: continue
                d['age'] = int(age);
                data[k] = d
            except:
                pass
        while True:
            y = input('--Chan I help you? [yes/no]')
            while not y:
                y = input('--Yes or no?')
            d['history'].append(y);
            data[k] = d
            if y in {'no', 'No', 'n', 'N'}:
                print('--%s.' % y)
                print('--Bye bye.')
                break
            elif y in {'yes', 'Yes', 'y', 'Y'}:
                print('--%s.' % y)
                print('I am pleased to serve you.')
            else:
                print('I am sorry. I can not understand what you said.')
                break

            # save data
    y = input('--Do you want to save the data? [yes/no]')
    while not y:
        y = input('--Yes or no?')
    if y in {'no', 'No', 'n', 'N'}:
        print('--%s. [You say no.]' % y)
    elif y in {'yes', 'Yes', 'y', 'Y'}:
        print('--%s. [the data is saved in file named "data".]' % y)
        save_data(data, 'data')
    else:
        print('I am sorry. I can not understand what you said. data are not saved.')

