#!/usr/bin/env python3
#-*- cording: utf-8 -*-
import WSServer

if __name__ == '__main__':
    ip = "192.168.11.128"
    port = 9001
    ws_server = WSServer.WSServer(ip, port)
    ws_server.run()