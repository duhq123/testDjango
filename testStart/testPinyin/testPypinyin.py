# coding=utf-8
import os

from pypinyin import pinyin, lazy_pinyin, Style
from pypinyin.style import register

@register('kiss')
def kiss(pinyin, **kwargs):
    return '😘 {0}'.format(pinyin)


def get_word():
    file = 'word.json'
    # print(os.path.abspath(os.path.dirname(__file__)))
    # filepath = os.path.abspath(file)
    # f = open(filepath, 'r')
    f = open(file, 'r')
    # print(f)
    pinyin_key = {}
    for i in f.readlines():
        if 'pinyin' in i :
            py_key = i.replace('"pinyin": "', '').replace('",', '').strip()
            if py_key not in pinyin_key:
                pinyin_key.setdefault(py_key, 0)
    f.close()
    print(pinyin_key)
    return pinyin_key

if __name__ == '__main__':
    # print(pinyin(
    #     ' 不敢面对现实，故作沉睡！逃避奋斗的过程，极其懦弱。时常做梦，是一种完全清醒的梦，梦想着奇迹出现，梦想人生路上，障碍自动清零，梦想脚下是平坦的康庄大道，梦想没有荆棘没有沟壑的人生路。可梦终究是梦，总有醒来的一天，睁开眼睛的那一刻，既然发现，脚下的那块，长长的巨石还在那里，阻挡着自己前行的脚步，前方那个半米宽的沟壑还在那里。这一切的一切，自己怎能不知，脚下障碍，没有人会帮自己去清理，但懦弱的自己，不敢面对眼前这一切，无限拖延着，不愿去推那块石头进前方的沟壑，害怕自己推不动，即使明白，不推是永远也不会知道，自己是否能推动，然而就是害怕失败，不去行动。于是闭上眼睛，等待着等待着上天的垂帘。自己如此虔诚，如此明白事理，如此这般的渴望达成的目标，上天怎能不眷顾，怎么可以不对自己好一点，怎么可以不帮自己，清理人生路上的障碍呢！我是明白世间真谛的人，我是能够把握，做好一件事情所有的规则和步骤。为什么不帮我清除障碍，倘若帮我清除障碍，我一定会做出一番令人艳羡的成绩。然而内心明白这样一道理，知道一件事怎么做，不一定代表你就会做了。当一个人，告诉你游泳时，手怎么划，脚该怎么动，你记住全部姿势，不会游泳的你，觉得此时学会游泳了吗？你如同小昭，背会乾坤大挪移心法，便能成为武林高手吗？考驾照，考完科一，熟悉所有交通规则，如此可以开车呢。一个人明白做事的规则，知道做事的步骤，不一定会做事！其实你明白，不愿意承认而已！有人说你异想天开，等着天上掉馅饼，你必定会反驳：你们怎么可以说，我是这种人，我怎会是这种人，我从来就没有想过，不劳而获，我所追求的，是通过自己的努力获得。'))

    #########################
    # meme = lazy_pinyin('亲亲', style='kiss')
    # print(meme)
    # print(pinyin('还没'))

    #########################
    get_word()