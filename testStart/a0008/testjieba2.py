# encoding=utf-8
import jieba
if __name__ == '__main__':

    st = '案件通知否定还领一个隐藏买发票买发票礼品对搭配给他猛干猛更可取。'
    print(st)

    seg_list = jieba.cut(st, cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

    seg_list = jieba.cut(st, cut_all=False)
    print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

    seg_list = jieba.cut(st)  # 默认是精确模式
    print(", ".join(seg_list))

    seg_list = jieba.cut_for_search(st)  # 搜索引擎模式
    print(", ".join(seg_list))
