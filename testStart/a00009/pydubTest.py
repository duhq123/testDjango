# import speech_recognition as sr

from pydub import AudioSegment
from pydub.silence import detect_silence, split_on_silence
import re

# from tjtts.aiqqasrapi import AiQQAsrApi

if __name__ == '__main__':
    # filepath = '/Users/edz/Desktop/chesunxian.wav'
    filepath = '/Users/edz/Desktop/Rec01201811091411244020.wav'

    sound = AudioSegment.from_file(filepath, format="wav")

    start_end = detect_silence(sound,100,-35,1)

    str1 = "\n".join('%s' %id for id in start_end)

    str2 = re.findall(r" (.+?)]",str1)

    str3 = "\n".join('%s' %id for id in str2)
    str4 = []
    idd = 0
    for sss in str3.split():
        dd = int(sss) - idd
        m,ms = divmod(float(sss),60000)
        s,ms = divmod(float(ms),1000)
        ts="%02d:%02d.%03d" % (m,s,ms)
        if(idd>1100):
            str4.append(ts)
        idd = int(sss)


    str5 = "\n".join('[%s]' %id for id in str4)

    with open('/Users/edz/Desktop/Q2lrc.txt', 'w') as f:
        f.write(str5)
    f.close()
    # for i in f.readlines():
    #     print(i)

    print(str2)
    print(str3)
    print(str4)


    voice = AudioSegment.from_wav(filepath)
    print(voice.channels)
    voice2 = AudioSegment.empty()
    voice3 = AudioSegment.empty()
    second_beg = 0
    second_end = 0
    for i in str1.split('\n'):
        # print(i.split(','))
        if second_beg == 0:

            second_beg = int(i.split(',')[0][1:])
            second_end = int(i.split(',')[1][:-1])
            voice2 = voice[:second_beg] + voice2
            voice = voice[second_beg:]
        else:
            print()
        # print(i.split(',')[0][1:], i.split(',')[1][:-1])
        # voice2 = voice[second_beg:second_end] + voice2
        # print(len(voice2))
        # voice = voice[second_end:]


    print(len(voice2))
    voice2.export('/Users/edz/Desktop/1.wav', format='wav')
    # print(str2)
    # print(str3)
    # print(str4)
    # print(str5)
    # print(f)