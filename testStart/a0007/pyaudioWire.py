# """
# PyAudio Example: Make a wire between input and output (i.e., record a
# few samples and play them back immediately).
#
# This is the callback (non-blocking) version.
# """
#
# import pyaudio
# import time
#
# WIDTH = 2
# CHANNELS = 2
# RATE = 44100
#
# p = pyaudio.PyAudio()
#
# def callback(in_data, frame_count, time_info, status):
#     return (in_data, pyaudio.paContinue)
#
# stream = p.open(format=p.get_format_from_width(WIDTH),
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 output=True,
#                 stream_callback=callback)
#
# stream.start_stream()
#
# while stream.is_active():
#     time.sleep(0.1)
#
# stream.stop_stream()
# stream.close()
#
# p.terminate()


"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).
"""

import pyaudio

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