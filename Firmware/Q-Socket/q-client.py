#!/usr/bin/env python3
#-*- cording: utf-8 -*-
import WSClient
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        host = "ws://192.168.11.128:9001/"
    else:
        host = sys.argv[1]
    
    ws_client = WSClient.WSClient(host)
    ws_client.run_forever()