#coding:utf-8
import pygame.mixer
import time
import threading
import os

flag = True

def wait_input():
    global flag
    input()
    flag = False

def generate():
    global flag
    while flag:
        os.system('docker-compose run magenta python3 /magenta-data/generate/composition.py')
        print('generate end')
        time.sleep(120)

def sound():
    global flag
    th = threading.Thread(target=wait_input)
    th.start()
    gen = threading.Thread(target=generate)
    current_path = os.path.dirname(os.path.abspath(__file__))+'/src/generate'
    print(current_path)
    #time.sleep(16)
    print('generate start')
    gen.start()
    pygame.mixer.init() #初期化

    while flag:
        print('play')
        if not os.path.exists(current_path+'/composition/'):
            os.mkdir(current_path+'/composition/')
        if not os.path.exists(current_path+'/play/'):
            os.mkdir(current_path+'/play/')
        if not os.path.exists(current_path+'/archive/'):
            os.mkdir(current_path+'/archive/')
        if os.path.isfile(current_path+"/composition/composition.mp3"):
            if os.path.isfile(current_path+"/play/music.mp3"):
                os.rename(current_path+"/play/music.mp3", current_path+"/archive/"+str(time.time())+".mp3")
            # MIDIファイル移動
            os.rename(current_path+"/composition/composition.mp3", current_path+"/play/music.mp3")
            pygame.mixer.music.load(current_path+"/play/music.mp3") #読み込み
        elif os.path.isfile(current_path+"/play/music.mp3"):
            pygame.mixer.music.load(current_path+"/play/music.mp3") #読み込み
        else:
            print('generating')
            time.sleep(20)
            continue
        pygame.mixer.music.play(0) #再生
        time.sleep(120)
        pygame.mixer.music.fadeout(10000)
        continue

    th.join()
    gen.join()

    pygame.mixer.music.stop() #終了

if __name__ == '__main__':
    sound()