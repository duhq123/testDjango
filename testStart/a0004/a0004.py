# #coding=utf-8
#
import re


def get_word_frequencies(file_name):
    dic = {}
    txt = open(file_name, 'r', encoding='utf-8').read().splitlines()

    n = 0
    for line in txt:
        # print(line)
        line = re.sub(r'[.?!,""/]', ' ', line)  # 要替换的标点符号，英文字符可能出现的
        line = re.sub(r' - ', ' ', line)  # 替换单独的‘-’
        for word in line.split():

            # 当一行的最后一个字符是-的时候，需要跟下一个英文字符串联起来构成单词
            if word[-1] == '-':
                m = word[:-1]
                n = 1
                break
            if n == 1:
                word = m + word
                n = 0
            # print(word)
            dic.setdefault(word.lower(), 0)  # 不区分大小写
            dic[word.lower()] += 1
    print(dic)

    return dic


# get_word_frequencies("/Users/edz/Desktop/1.txt")
if __name__ == '__main__':
    get_word_frequencies("/Users/edz/Desktop/1.txt")
    # get_word_frequencies("/Users/edz/Desktop/test.txt")
    # get_word_frequencies("1.txt")

# import re
#
# with open('1.txt', 'r', encoding='utf-8') as f:
#     dictResult = {}
#
#     # Find the letters each line
#     for line in f.readlines():
#         listMatch = re.findall('[a-zA-Z]+', line.lower()) # remember to lower the letters
#
#         # Count
#         for eachLetter in listMatch:
#             eachLetterCount = len(re.findall(eachLetter, line.lower()))
#             dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount
#
#     # Sort the result
#     result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)
#     print(result)
# for each in result:
#     print(each)
