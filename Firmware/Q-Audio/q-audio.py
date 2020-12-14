#!/usr/bin/env python3
#-*- cording: utf-8 -*-
import pyaudio
import wave
import sys

def PlayWav(Filename = "sample.wav"):
    try:
        wf = wave.open(Filename, 'rb')
        print("Open file : " + Filename)
    except FileNotFoundError: #ファイルが存在しなかった場合
        print("[Error 404] No such file or directory: " + Filename)
        return 0
    
    # チャンク数を指定
    chunk = 2048 # 1024だとoverflowする
    # PyAudioのインスタンスを生成
    p = pyaudio.PyAudio()
    # Streamを生成
    """
    format: ストリームを読み書きする際のデータ型
    channels: モノラルだと1、ステレオだと2、それ以外の数字は入らない
    rate: サンプル周波数
    output: 出力モード
    """
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # データを1度に2048個読み取る
    data = wf.readframes(chunk)
    # 実行
    while data != b'':
        # ストリームへの書き込み
        stream.write(data)
        # 再度2048個読み取る
        data = wf.readframes(chunk)
    # ファイルが終わったら終了処理
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ is "__main__":
    if len(sys.argv) < 2:
        filename = "sample.wav"
    else:
        filename = sys.argv[1]
    PlayWav(filename) 