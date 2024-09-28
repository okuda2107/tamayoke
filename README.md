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
error.wav
pop.wav
result.json
title.png
GameProperty.json
get.mp3
level1.json
```

## 設定方法
asset内にあるjsonファイルは設定ファイルである．ゲームをプレイする際に自由に調整できる．
### GameProperty.json
ゲーム全体の設定
プロパティ名|説明
-|-
screenSize|ゲームウィンドウのサイズ
cameraCheck|trueにするとカメラの画角を調整するためのウィンドウが表示される
cameraNumber|default値は0．カメラデバイスが複数ついているときに1などの適当な番号を設定すると，その番号に対応したカメラでゲームができる

### level.json
ゲームの難易度設定
プロパティ名|説明
-|-
coreNum|赤いcoreの数
pointers|黄色い球を体のどこにつけるか指定できる．指定番号は以下の図と対応している．

![image](https://github.com/user-attachments/assets/65b0aba4-f7b2-4c45-9c53-4c659fb71fb4)

# For Developper

## 開発環境
python 3.9.13

## 開発環境構築
1. ソースコードをダウンロード
1. `python -m venv {venv_name}`
1. `source {venv_name}/bin/activate`でvenv起動 windowsの場合は`{venv_name}/Scripts/activate`
1. `pip install -r requirements.txt`をコマンドで叩く
1. `deactivate`でvenvから抜ける

## release方法
exeファイルを作ってリリース
1. pyinstallerをinstall
1. main.specファイルを書く
1. `pyinstaller main.spec`を叩く
1. main.exeができるので，assetと一緒にリリース
