import re
import datetime

def test(card_data):
    pattern = re.compile(r'\d+')
    match = pattern.findall(card_data)
    print(match)
    a, l, card_data1 = 0, 0, ''
    for i in range(len(match)):
        a = card_data[a:].find(match[i])
        b = len(match[i])
        text = card_data[l + a + b:]
        card_data = card_data[l:a + l] + '<figure>' + match[i] + '</figure>'
        card_data1 = card_data = card_data1 + card_data
        l = a = len(card_data)
        card_data = card_data + text
    print(card_data)


def tese_time(date):
    date1 = datetime.datetime.now().__format__('%Y-%m')
    print(date1>date or date1 == date)
    print(date1)
    date2 = datetime.datetime(year=datetime.datetime.now().year, month=datetime.datetime.now().month-1, day=1).__format__('%Y-%m')
    print(date2)

if __name__ == '__main__':
    # card_data = '京A555N55C5的骑车'
    # test(card_data)
    tese_time('2018-09')