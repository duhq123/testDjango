import pyaudio
import wave
import time
import sys

def paly():
    """PyAudio Example: Play a WAVE file."""
    CHUNK = 1024

    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


def save():
    """PyAudio example: Record a few seconds of audio and save to a WAVE file."""
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []
    flage = True
    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    while flage is True:
        data = stream.read(CHUNK)
        frames.append(data)
        flage = get_flage()

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def get_flage():
    return stop(None)

def stop(user):
    if user is None:
        flag = False
    return flag

def wire():
    """
    PyAudio Example: Make a wire between input and output (i.e., record a
    few samples and play them back immediately).
    """
    CHUNK = 1024
    WIDTH = 2
    CHANNELS = 2
    RATE = 44100
    RECORD_SECONDS = 5

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(WIDTH),
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        stream.write(data, CHUNK)

    print("* done")

    stream.stop_stream()
    stream.close()

    p.terminate()




def channelMap():
    chunk = 1024

    PyAudio = pyaudio.PyAudio

    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s output.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')

    p = PyAudio()

    # standard L-R stereo
    # channel_map = (0, 1)

    # reverse: R-L stereo
    # channel_map = (1, 0)

    # no audio
    # channel_map = (-1, -1)

    # left channel audio --> left speaker; no right channel
    # channel_map = (0, -1)

    # right channel audio --> right speaker; no left channel
    # channel_map = (-1, 1)

    # left channel audio --> right speaker
    # channel_map = (-1, 0)

    # right channel audio --> left speaker
    channel_map = (1, -1)
    # etc...

    try:
        stream_info = pyaudio.PaMacCoreStreamInfo(
            flags=pyaudio.PaMacCoreStreamInfo.paMacCorePlayNice, # default
            channel_map=channel_map)
    except AttributeError:
        print("Sorry, couldn't find PaMacCoreStreamInfo. Make sure that "
              "you're running on Mac OS X.")
        sys.exit(-1)

    print("Stream Info Flags:", stream_info.get_flags())
    print("Stream Info Channel Map:", stream_info.get_channel_map())

    # open stream
    stream = p.open(
        format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
        output_host_api_specific_stream_info=stream_info)

    # read data
    data = wf.readframes(chunk)

    # play stream
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()






def callBack():
    """
    PyAudio Example: Play a wave file (callback version).
    """


    if len(sys.argv) < 2:
        print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
        sys.exit(-1)

    wf = wave.open(sys.argv[1], 'rb')

    # instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    p.terminate()





if __name__ == '__main__':
    save()
    # wire()
    # channelMap()
    # callBack()