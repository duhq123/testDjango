# find the difference between tow texts
import difflib, sys, re, string


def checkTwoTexts(text1, text2):
    textLines1 = text1.splitlines(1)
    textLines2 = text2.splitlines(1)
    # print('text1')
    # pritLine(textLines1)
    # print('text2')
    # pritLine(textLines2)
    diff1 = difflib.ndiff(text1, text2)
    sys.stdout.writelines(diff1)
    # diff = list(difflib.Differ().compare(textLines1, textLines2))
    # for line in diff:
    #     print(line)
    return None


def pritLine(lines):
    for line in lines:
        print(line)


if __name__ == '__main__':
    text1 = '我们人保的这笔贷款是通过中国光大银行发放的是上人行征信报告的您现在逾期了肯定对您以后贷款去和银行打交道的所有业务都有影响，' \
            '而且现在借钱都很难工作找到了一时半会儿也没有工资，这也不是当前最好的解决办法，你负债多少，有考虑过卖房吗您可以前往我司柜' \
            '台直接办理也可以联系您的业务员代为办理如有其他疑问可致电我司客服热线95585进行咨询。请您及时办理续保手续，请问您清楚了吗'
    text2 = '我们人保的这笔贷款是通过中国光大银行发放的是上人行征信报告的您现在逾期了肯定对您以后贷款其和银行打交道的所有业务都有影响，' \
            '而且现在借钱都很难工作找到了一时半会儿也没有工资，这也不是当前最好的解决办法，你负债多少，有考虑过买房吗 你可以前往我司柜' \
            '台直接办理也可以联系您的业务员代为办理如有其他疑问可致电我司客服热线95585进行咨询，请您及时办理续保手续，请问您清楚了吗'
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~，。、！？："""""
    b1 = ''.join(c for c in text1 if c not in punctuation)
    b2 = ''.join(c for c in text1 if c not in punctuation)

    # print(b1,'\n',b2)

    # checkTwoTexts(b1, b2)
    checkTwoTexts(text1, text2)
