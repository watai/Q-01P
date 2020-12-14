#!/usr/bin/env python3
#-*- cording: utf-8 -*-
import websocket
from threading import Thread
import time
import sys

class WSClient:
    def __init__(self, host):
        # デバックログの表示/非表示設定
        websocket.enableTrace(False)

        # WebSocketAppクラスを生成
        # 関数登録のために、ラムダ式を使用
        self.ws = websocket.WebSocketApp(host,
            on_message = lambda ws, msg: self.on_message(ws, msg),
            on_error = lambda ws, msg: self.on_error(ws, msg),
            on_close = lambda ws: self.on_close(ws))
        self.ws.on_open = lambda ws: self.on_open(ws)
    
    # メッセージ受信に呼ばれる関数
    def on_message(self, ws, message):
        print("receive : {}".format(message))
    
    # エラー時に呼ばれる関数
    def on_error(self, ws, error):
        print(error)
    
    # サーバーから切断時に呼ばれる関数
    def on_close(self, ws):
        print("### closed ###")

    # サーバーから接続時に呼ばれる関数
    def on_open(self, ws):
        Thread(target=self.run).start()

    # サーバーから接続時にスレッドで起動する関数
    def run(self, *args):
        while True:
            # pass
            time.sleep(0.1)
            input_data = input("send data:")
            self.ws.send(input_data)

        self.ws.close()
        print("Thread terminating...")

    # websocketクライアント起動
    def run_forever(self):
        self.ws.run_forever()

    def send(self, message):
        self.ws.send(message)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        host = "ws://192.168.11.128:9001/"
    else:
        host = sys.argv[1]
    
    ws_client = WSClient(host)
    ws_client.run_forever()