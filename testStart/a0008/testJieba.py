import jieba
import re, csv, os


def test(paragraph):
    sentences = re.split('(。|！|\!|\.|？|\?)', paragraph)  # 保留分割符

    new_sents = []
    for i in range(int(len(sentences) / 2)):
        sent = sentences[2 * i] + sentences[2 * i + 1]
        new_sents.append(sent)

    # print(new_sents)
    return new_sents


def test2(paragraph):
    sentence = re.split('。|！|\!|\.|？|\?', paragraph)  # 不保留分割符

    new_sents = []
    for i in range(int(len(sentence) / 2)):
        sent = sentence[2 * i] + sentence[2 * i + 1]
        new_sents.append(sent)

    # print(new_sents)
    return new_sents


if __name__ == '__main__':

    # 输入一个段落，分成句子，可使用split函数来实现
    paragraph = "生活对我们任何人来说都不容易！我们必须努力，最重要的是我们必须相信自己。 \
    我们必须相信，我们每个人都能够做得很好，而且，当我们发现这是什么时，我们必须努力工作，直到我们成功。"
    file_name = 'sub-new-clause.csv'
    target = os.path.join('/Users/edz/Desktop', file_name)

    file_object = open('/Users/edz/Desktop/zh_new_all.txt', 'r')
    words = []
    a = ''
    for line in file_object.readlines():
        words.append(line)
    back_str = str(test(str(words)))

    rep = {'\"': '', '\'': '', '\\\\xa0': '', '\\\\n': '', '\\\\u200b': ''}

    rep = dict((re.escape(k), v) for k, v in rep.items())

    pattern = re.compile("|".join(rep.keys()))

    my_str = pattern.sub(lambda m: rep[re.escape(m.group(0))], back_str)

    with open(target, 'w+') as f1:
        writer = csv.writer(f1)
        # b = 1
        for i in str(my_str).split(','):
            print(len(i))
            if len(i) > 40:
                # writer.writerow([b, i])
                writer.writerow([i.strip()])
                # b += 1
            elif len(i) > 6:
                a += i.strip()
                if len(a) > 40:
                    # writer.writerow([b, a])
                    writer.writerow([a.strip()])
                    a = ''
                    # b += 1
    print('ending............')
    file_object.close()
