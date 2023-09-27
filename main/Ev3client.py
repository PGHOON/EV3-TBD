#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket
import subprocess

lcd = Screen()
btn = Button()

Server_Addr = ('192.168.2.2', 12344)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(Server_Addr)
lcd.clear()
lcd.draw.text((10, 5), 'Connecting to Server ...')
lcd.update()

while True:
    lcd.clear()
    lcd.draw.text((10, 5), 'Connected!!!')
    lcd.update()
    client.send('...'.encode())
    if btn.right:
        client.send(':right'.encode())
        file_path = "/home/robot/socket_test/webcam.jpg"
        command = ["fswebcam", "--no-banner", "--resolution", "480x480", "--save", file_path]
        subprocess.run(command)

        with open('webcam.jpg', 'rb') as file:
            file_size = len(file.read())
            client.send(str(file_size).encode())
            file.seek(0)
            while True:
                data = file.read(1024)
                if not data:
                    break
                client.send(data)

file.close()
client.close()