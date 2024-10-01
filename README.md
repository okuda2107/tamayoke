# tama.yoke
プレイヤーは自分の体にくっついた黄色い球を操作して，赤い球をよけながら，白い点にぶつけて消していく．<br>
白い点は赤い球めがけて飛んでいき，白と赤が接触したらゲームオーバー．

![{F5AABDCE-7FC9-4AD1-8EBB-A1021851B1D6}](https://github.com/user-attachments/assets/f7ddd5b9-bc68-43df-86c6-d4316ee2dc21)

https://github.com/user-attachments/assets/45857d47-c42a-459f-a09b-193598cdabe5


## 遊び方
環境はwindows11を想定しています．カメラを用いるので，カメラデバイスがついていないと起動できません．
1. リリースページからgame.zipをダウンロード．展開します．
1. 圧縮してあった状態のディレクトリ構成のまま実行ファイルを実行します．具体的には以下のような構成．
```
asset/
main.exe
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
