
import fnmatch, os
# from pydub import AudioSegment
#
# def wav_8k_to_16k(wav_file: str):
#     sound = AudioSegment.from_wav(wav_file)
#     wav_file = '{0}.wav'.format(os.path.splitext(wav_file)[0])
#     s = sound.set_frame_rate(16000)
#     s.export(wav_file, format='wav')
#     return wav_file
from tjtts.VoiceUtils import wav_8k_to_16k

if __name__ == '__main__':
    dirname = '/Users/edz/Desktop/yuyinshibie/huashu'
    for file in os.listdir(dirname):
        if fnmatch.fnmatch(file, '*.wav'):
            path = os.path.join(dirname, file)
            wav_8k_to_16k(path)
            # add_volume(path, -3)