# -*- coding:UTF-8 -*-
import re

import requests
from bs4 import BeautifulSoup


def replace_str(rep, words):
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    my_str = pattern.sub(lambda m: rep[re.escape(m.group(0))], words)
    return my_str


if __name__ == '__main__':



    url = 'https://www.tutorabc.com.cn/About/NewsDetail/8593.html'
    req = requests.get(url)
    html = req.text

    div_bf = BeautifulSoup(html, 'html.parser')
    # div = div_bf.find_all('div', class_ = 'content_container')
    # div = div_bf.find_all('div', class_ = 'news_container')
    div_c = div_bf.find_all('div', id = 'divContent')
    div_pf = BeautifulSoup(str(div_c[0]), 'html.parser')
    # print(div_pf)
    div_p = div_pf.find_all('p')
    rep = {'<p>': '', '</p>': '', '<br/>': '', '<div>': '', '</div>': '', '\n': ''}
    for i in div_p:
        data = replace_str(rep, str(i))
        if 'style' not in data:
            print(data)





