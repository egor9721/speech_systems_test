import speech_recognition as sr
import time
from pydub import AudioSegment
from pydub.utils import make_chunks
import os


chunk_path = os.path.join('..\\audio\\cache')  # временная папка с нарезанными аудио
if os.path.exists(chunk_path) is False:
    os.mkdir('..\\audio\\cache')


def create_chunks(audio_file, chunk_path):
    '''Разбиение аудиодорожки на части,
    на вход подаются записи формата wav'''
    my_audio = AudioSegment.from_file(audio_file, 'wav')
    chunk_length_ms = 60000  # длительность нарезки аудио в мс
    chunks = make_chunks(my_audio, chunk_length_ms)

    # экспорт в папку
    for i, chunk in enumerate(chunks):
        chunk_name = '{0}.wav'.format(i)
        print('exporting {}'.format(chunk_name))
        chunk.export(os.path.join(chunk_path, chunk_name), format='wav')


def delete_cache(cache_path):
    '''удаление кеша, сознданного при распознавании'''
    num_files = len([f for f in os.listdir(cache_path) if os.path.isfile(os.path.join(cache_path, f))])
    for i in range(num_files):
        file = os.path.join(cache_path, '{}.wav'.format(i))
        os.remove(file)


def recognizing(audio_path, file_path):
    recognizer = sr.Recognizer()
    num_files = len([f for f in os.listdir(audio_path) if os.path.isfile(os.path.join(audio_path, f))])
    print('start recognizing')
    with open(file_path, 'w', encoding='utf-8') as f:
        for i in range(num_files):
            audio = os.path.join(audio_path, '{}.wav'.format(i))
            sample_audio = sr.AudioFile(audio)
            print('recognition {0} out of {1}'.format(i+1, num_files))
            with sample_audio as audio_file:
                audio_content = recognizer.record(audio_file)
            f.write(recognizer.recognize_google(audio_content, language='ru-RU').lower())
        print('recognizing sucsessfully')


def start_recognition(audio_file, text_file):
    time_for_recognition = []
    start_time = time.time()
    create_chunks(audio_file, chunk_path)
    recognizing(audio_path=chunk_path, file_path=text_file)
    delete_cache(chunk_path)
    finally_time = (time.time()-start_time)/60
    time_for_recognition.append(finally_time)
    print('------ {:.2} minutes -------'.format(finally_time))
