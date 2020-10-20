from pydub import AudioSegment
import os
import re

print('enter .mp3 file for conversation')
audio_name = input()
basename = os.path.basename(audio_name)
print('enter path with converted audio')
output_path = input()
output_name = os.path.join(output_path, re.sub('wav', 'wav', basename))
sound = AudioSegment.from_wav(os.path.join(audio_name))
sound_mono = sound.set_channels(1)
sound_mono.export(output_name, format='wav')