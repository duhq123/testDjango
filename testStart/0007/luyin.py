# -*- coding：utf-8 -*-
import pyaudio
import wave

input_filename = "input.wav"  # 麦克风采集的语音输入
input_filepath = "/Users/edz/Desktop/"  # 输入文件的path
in_path = input_filepath + input_filename


def get_flage():
    return stop(None)


def stop(user):
    import random
    num = random.randint(0, 1000)
    # if user is None:
    #     flag = False
    if num == 0:
        flag = False
    else:
        flag = True
    print(num, flag)
    return flag


def start_init():
    CHUNK = 256
    FORMAT = pyaudio.paInt16
    CHANNELS = 1  # 声道数
    RATE = 16000  # 采样率

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)


    print(stream)
    return CHUNK, RATE, stream, p


def start_save(second, CHUNK, RATE, stream, frames, num):
    print("*" * 10, f"开始录音：请在{second}秒内输入语音")
    # WAVE_OUTPUT_FILENAME = filepath
    RECORD_SECONDS = second
    frames = frames
    flage = True
    # while flage:
    if num != 1:
        stream.start_stream()
    while flage:
    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
        flage = get_flage()
        if flage is False:
            break
    print("*" * 10, "录音结束\n")

    stream.stop_stream()
    return frames, stream


def close_save(p, frames, stream, filepath, rate):
    FORMAT = pyaudio.paInt16
    WAVE_OUTPUT_FILENAME = filepath
    CHANNELS = 1  # 声道数
    RATE = rate

    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

# 联合上一篇博客代码使用，就注释掉下面，单独使用就不注释
if __name__ == '__main__':
    chunk, rate, stream, p = start_init()
    frames = []
    # for i in range(0, 10):
    frames, stream = start_save(second=50, CHUNK=chunk, RATE=rate, stream=stream, frames=frames, num=1)
    # restart_save(stream, frames, sencod=50)
    # restart_save
    frames, stream = start_save(second=50, CHUNK=chunk, RATE=rate, stream=stream, frames=frames, num=2)
    close_save(p=p, stream=stream, frames=frames, filepath=in_path, rate=rate)
