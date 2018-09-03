import re

def test(str):
    # str = 'aaaasdasdas546456sfdsa123dasdad11asda1dasd2dasd'
    pattern = re.compile(r'\d+')
    match = pattern.findall(str)
    print(match)
    for i in range(match.__len__()):
        if len(match[i]) > 1:
            a = str.index(match[i])
            b = len(match[i])
            str = str[0:a] + '<a>' + match[i] + '</a>' + str[a + b:]
        # print(str)
    print(str)


if __name__ == '__main__':
    # str = '京A23B45'
    # str = '京A2B345'
    str = '京A2B34N'
    # str = 'aaaasdasdas546456sfdsa123dasdad11asda1dasd2dasd'
    test(str)
