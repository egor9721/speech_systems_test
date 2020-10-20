import vosk_short
import speech_for_google
import os
import re


def start():
    print('===============================================')
    print('===============================================')
    print('========= pre-alpha speech recognition ========')
    print('===============================================')

    print('\nNow you can only translate audio in text')


def choice():
    print('you can translate audio using the Google Speech Recognition (1), local (2) or Yandex SpeechKit (3)?')
    print('enter 0 to exit')

    while True:
        print('print your change')
        answer = int(input())
        if answer == 1 or answer == 2 or answer == 3:
    
            print('insert path to file')
            input_file = input()
            input_file = os.path.abspath(input_file)
            if os.path.exists(input_file) is False:
                print('uncorrect path')
                continue
    
            print('insert path to output file')
            output_file = input()
            if os.path.exists(output_file) is False:
                output_file = os.path.join('..\\text')
                print('output file will be saved to path: ', output_file)
            basename = os.path.basename(input_file)
            basename = re.sub('wav', 'txt', basename)
            output_file = os.path.join(output_file, basename)
            output_file = os.path.abspath(output_file)


            return answer, input_file, output_file
        elif answer == 0:
            exit()
        else:
            print('uncorrect answer')


start()

while True:
    answer, input_file, output_file = choice()
    if answer == 1:
        speech_for_google.start_recognition(input_file, output_file)
    elif answer == 2:
        vosk_short.start(input_file, output_file)
    elif answer == 3:
        yandex_speech2text.start(input_file, output_file)

    

