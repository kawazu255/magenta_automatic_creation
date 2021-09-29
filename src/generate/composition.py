import pretty_midi
from glob import glob
import os
import time
import subprocess
import threading
from scipy.io import wavfile

base_dir = '/magenta-data/'
improv＿dir_name = base_dir+'generate/improv/'
drums＿dir_name = base_dir+'generate/drums/'

flag = True

def wait_input():
    global flag
    input()
    flag = False

def generate():
    global improv＿dir_name
    global drums＿dir_name
    #th = threading.Thread(target=wait_input)
    #th.start()
    os.system('python /magenta/magenta/models/drums_rnn/drums_rnn_generate.py --config=drum_kit --bundle_file=/magenta-data/generate/drum_kit_rnn.mag --output_dir=/magenta-data/generate/drums --num_outputs=1 --num_steps=1024 --primer_drums="[(36,)]"')
    os.system('python /magenta/magenta/models/improv_rnn/improv_rnn_generate.py --config=chord_pitches_improv --bundle_file=/magenta-data/generate/chord_pitches_improv.mag --output_dir=/magenta-data/generate/improv --num_outputs=1 --primer_melody="[69]" --backing_chords="FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7 FM7 E7 Am7 C7" --render_chords')
    composite()
    # ファイル削除
    remove_midi(improv＿dir_name)
    remove_midi(drums＿dir_name)
    #th.join()

def composite():
    global improv＿dir_name
    global drums＿dir_name
    # MIDIファイルを読み込む
    improv_data = get_midi(improv＿dir_name)
    drums_data = get_midi(drums＿dir_name)
    if improv_data is None or drums_data is None:
        exit(0)

    # メロディの音色変更
    # ピアノ
    improv_data.instruments[0].program = 1
    improv_data.instruments[1].program = 33

    # 弦楽器
    #improv_data.instruments[0].program = 41
    #improv_data.instruments[1].program = 50

    # オルゴール癒し
    #improv_data.instruments[0].program = 11
    #improv_data.instruments[1].program = 11

    # フルート
    #improv_data.instruments[0].program = 74
    #improv_data.instruments[1].program = 50

    # 金管楽器
    #improv_data.instruments[0].program = 57
    #improv_data.instruments[1].program = 50

    # 楽器の一覧
    print(improv_data.instruments)
    print('')
    print(drums_data.instruments)

    # improveとdrumを合成する
    for instrument in drums_data.instruments:
        improv_data.instruments.append(instrument)

    # 保存する
    if not os.path.exists('generate/composition/'):
        os.mkdir('generate/composition/')
    improv_data.write('generate/composition/composition.mid')
    pm = pretty_midi.PrettyMIDI('generate/composition/composition.mid')
    audio_data = pm.fluidsynth(sf2_path='generate/SGM-V2.01.sf2')
    wavfile.write("generate/composition/pre_composition.wav",44100, audio_data)
    #os.system("ffmpeg -i generate/composition/pre_composition.wav -acodec pcm_u8 generate/composition/composition.wav")
    os.system('ffmpeg -i "generate/composition/pre_composition.wav" -vn -ac 2 -ar 44100 -ab 256k -acodec libmp3lame -f mp3 "generate/composition/composition.mp3"')

def get_midi(dir_name):
    for file in glob(dir_name + '/*.mid'):
        if os.path.exists(file):
            print(file)
            return pretty_midi.PrettyMIDI(file)
    return None

def remove_midi(dir_name):
    for file in glob(dir_name + '/*.mid'):
        if os.path.exists(file):
            os.remove(file)

if __name__ == '__main__':
    generate()