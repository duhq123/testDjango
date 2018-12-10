# coding=utf-8


def cut_sentence_new(words):
    # words = (words).decode('utf8')
    start = 0
    i = 0
    sents = []

    punt_list = ',.!?:;~，。！？：；～'.encode('utf8')
    for word in words:
        if word in punt_list and token not in punt_list:  # 检查标点符号下一个字符是否还是标点
            sents.append(words[start:i + 1])
            start = i + 1
            i += 1
        else:
            i += 1
            token = list(words[start:i + 2]).pop()  # 取下一个字符
    if start < len(words):
        sents.append(words[start:])
    return sents


if __name__ == '__main__':
    file_object = open('/Users/edz/Desktop/zh.txt')
    words = []
    for line in file_object:
        words.append(line)

    print(words)
    cut_sentence_new(words=words)
