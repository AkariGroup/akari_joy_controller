# akari_joy_controller

AKARIのヘッドをジョイスティックで動かすアプリ

## 仮想環境の作成
`python -m venv venv`  
`source venv/bin/activate`  
`pip install -r requirements.txt`  

## アプリの起動
AKARIにジョイスティックを接続し、アプリを起動します。  
`python3 joy_controller.py`  

## 使い方
上下左右のジョイスティック操作で、AKARIのヘッドが上下左右に動きます。  
0ボタンを押すと、AKARIのヘッドが初期位置に戻ります。  
