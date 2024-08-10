# tama|wake
球を仕分けるゲームです

## 遊び方
実行ファイルを実行します．この時フォルダ構成を以下のようにしておく
```
$ ls -R
.:
asset
main.exe

./asset:
Cosmic_Fantasy.mp3
bar.png
error.wav
playground.json
pop.wav
result.json
title.png
GameProperty.json
entrypoint.png
get.mp3
pointer.png
red.png
title.json
white.png
```

## 設定方法
asset内にあるjsonファイルは設定ファイルである．ゲームをプレイする際に自由に調整できる．
### GameProperty.json
ゲーム全体の設定
プロパティ名|説明
-|-
screenSize|ゲームウィンドウのサイズ
cameraCheck|trueにするとカメラの画角を調整するためのウィンドウが表示される

### title.json
タイトル画面の設定
プロパティ名|説明
-|-
position|タイトルロゴの位置
startSize|スタートオブジェクトのサイズ
size|タイトルロゴのサイズ

### playground.json
ゲーム画面の設定
プロパティ名|説明
-|-
timerSize|画面上のタイマーとスコアのテキストの大きさ

### result.json
リザルト画面の設定
プロパティ名|説明
-|-
position|リザルト画面の数字の位置
scoreSize|数字の大きさ
textPos|"Your Score is"の文字の位置
textSize|"Your Score is"の文字の大きさ

## 開発環境
python 3.9.13

## 開発環境構築
1. ソースコードをダウンロード
1. `python -m venv {venv_name}`
1. `source {venv_name}/bin/activate`でvenv起動 windowsの場合は`{venv_name}/Scripts/activate`
1. `pip install -r requirements.txt`をコマンドで叩く
1. `deactivate`でvenvから抜ける
