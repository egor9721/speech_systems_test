import requests
import time
import os


def record(i, start_time, audio_path, params=60):

    name = os.path.join(audio_path+'\\segment'+str(i)+'.mp3')
    data = open(name, 'wb')
    print('segment {} recording'.format(i))
    for block in r.iter_content(1024):
        data.write(block)
        end_time = time.time()
        if end_time-start_time >= params:
            data.close()
            print('segment record sucsessful')
            break


# формирование ссылки для стрима
print('enter URL station for Radio Garden')
user_link = input()
radio_id = user_link[user_link.rfind('/')+1:]
stream_url = 'http://radio.garden/api/ara/content/listen/' + radio_id + '/channel.mp3'

# установка длительности сегмента записи
print('enter time for one audio-segment, sec')
long_time = int(input())

# путь к папке сохранения
print('enter folder for save audio-segments')
user_path = str(input())

if os.path.exists(user_path) is False:
    os.mkdir(user_path)

r = requests.get(stream_url, stream=True)

i = 1  # номер первого сегмента
while True:
    '''процесс записи радио'''
    try:
        start_time = time.time()
        record(i, start_time, user_path, params=long_time)
        i += 1
    except KeyboardInterrupt:
        break
