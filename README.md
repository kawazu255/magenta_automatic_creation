# magenta_automatic_creation
Google Magentaを用いた音楽の自動生成&自動再生スクリプト。
スクリプト実行中、音楽mp3ファイルを自動で生成し続け、それを自動で再生し続けます。
スクリプトを停止するにはEnterキーを押してください。(すぐには止まりませんが、その時点で再生されている音楽を再生し切ったら止まります。)
Python3.6環境にて動作を確認しています。

## セットアップ方法
1. [こちら](https://ja.osdn.net/projects/sfnet_androidframe/downloads/soundfonts/SGM-V2.01.sf2/)からサウンドフォントファイルをダウンロードし、`src/generate/`配下に設置する
2. [こちら](http://download.magenta.tensorflow.org/models/chord_pitches_improv.mag)からコード&伴奏パート生成用モデルをダウンロードし、、`src/generate/`配下に設置する
3. [こちら](http://download.magenta.tensorflow.org/models/drum_kit_rnn.mag)からドラムパート生成用モデルをダウンロードし、、`src/generate/`配下に設置する
4. `pip install pygame`などでpygameを手元のPC環境にインストールする
5. docker-compose.ymlのあるディレクトリに移動し、`docker-compose build`する
6. 同じディレクトリで`python play.py`を実行すると、音楽を自動生成&自動再生し続けます。

## 特記事項
- 初回実行時には音楽の生成に時間がかかるため、約1分ほど音楽が再生されない時間があります。
- 2回目以降に実行する際は、前回スクリプト終了直前に生成された音楽を再生します。
- コード進行や音色を変更する場合は、`src/generate/composition.py`を編集してみてください。
- BPMを変更する場合は、`src/generate/constants.py`の`DEFAULT_QUARTERS_PER_MINUTE`を編集してみてください。
