from vosk import Model, KaldiRecognizer
import re
import os
import wave
import time

'''локальный перевод аудиофайла с помощью vosk-api
    принцип работы программы:
    1. проверяется возможность подключения к языковой модели модели
    2. проверяется формат файла (необходим формат wav с mono каналом и кодеком PCM)
    3. идет распознавание аудио'''


def start(input_filename, output_filename):
    time_for_recognition = [] # потраченное время на распознавание
    start_time = time.time()

    if not os.path.exists('..\\models\\vosk-model-ru-0.10'):  # проверка пути, где расположена модель
        print('Please download the model from https://alphacephei.com/vosk/models.html')
        exit(1)

    wf = wave.open(input_filename)
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":  # проверка формата аудио
        print('audio file must be WAV format mono PCM.')
        exit(1)

    model = Model('..\\models\\vosk-model-small-ru')  # выбор модели распознавания
    rec = KaldiRecognizer(model, wf.getframerate())

    with open(output_filename, 'w', encoding='utf-8') as f:
        while True:

            data = wf.readframes(1000)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                prerecord = rec.Result()
                prerecord_2 = re.split(r'"text" :', prerecord)  # тип данных list
                prerecord_2[1] = re.sub(r'[^а-яА-я0-9a-zA-Z ]', '', prerecord_2[1])  # чистка строки от спец символов
                print(prerecord_2[1])  # вывод отформатированной фразы
                f.write(prerecord_2[1] + '\n')  # запись результата распознавания
            else:
                pass

    finally_time = (time.time() - start_time) / 60
    time_for_recognition.append(finally_time)
    print('------ {:.2} minutes -------'.format(finally_time))