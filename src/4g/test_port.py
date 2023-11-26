#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket  # 导入 socket 模块
import time

s = socket.socket()  # 创建 socket 对象
# host = "115.195.90.17"  # 获取本地主机名
# port = 25525  # 设置端口号
host = "39.105.103.190"  # 获取本地主机名
port = 8618  # 设置端口号

s.connect((host, port))
# s.send("AA0510B1800006".encode())
s.send("AT+LIST\r\n".encode())
print("sent successfully")

print(s.recv(32))
# time.sleep(60)
s.close()
