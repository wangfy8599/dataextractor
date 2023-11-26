#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket  # 导入 socket 模块
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建 socket 对象
print('Socket created')

# host = "192.168.124.22"  # 获取本地主机名
host = "192.168.1.5"  # 获取本地主机名
port = 333  # 设置端口号

s.bind((host, port))
print('Socket bind complete')

s.listen(10)

while True:
    print('Socket now listening')
    conn, addr = s.accept()
    with conn:
        print('Connected with ' + addr[0] + ':' + str(addr[1]))
        while True:
            data = conn.recv(1024)
            if not data:
                print("connection reset")
                break
            print("received {}".format(data))
            conn.sendall(b"OK")

