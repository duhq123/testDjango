from pydub import AudioSegment

if __name__ == '__main__':

    sound1 = AudioSegment.from_file("/Users/edz/Desktop/中国平安客服电话@021 95512_20181102090318.amr", format="amr")
    # sound1 = AudioSegment.from_file("/Users/edz/PycharmProjects/untitled/testStart/0008/tjhb_2_1541408341652.7302.wav", format="wav")
    #默认mp3格式 中国平安客服电话@021 95512_20181102090318.amr
    duration_in_milliseconds = len(sound1)/1000  # 获取sound的时长
    print(duration_in_milliseconds)



