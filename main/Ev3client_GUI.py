#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket
import subprocess

lcd = Screen()
btn = Button()

Server_Addr = ('', 12333)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(Server_Addr)
lcd.clear()
lcd.draw.text((10, 5), 'Connecting to Server ...')
lcd.update()

while True:
    lcd.clear()
    lcd.draw.text((10, 5), 'Waiting Command...')
    lcd.update()
    data = client.recv(1024).decode()
    if data == 'Forward':
        lcd.clear()
        lcd.draw.text((10, 5), 'Forward')
        lcd.update()
        """Motor Control"""

    elif data == 'Backward':
        lcd.clear()
        lcd.draw.text((10, 5), 'Backward')
        lcd.update()
        """Motor Control"""

    elif data == 'Left':
        lcd.clear()
        lcd.draw.text((10, 5), 'Left')
        lcd.update()
        """Motor Control"""

    elif data == 'Right':
        lcd.clear()
        lcd.draw.text((10, 5), 'Right')
        lcd.update()
        """Motor Control"""

    elif data == 'Stop':
        lcd.clear()
        lcd.draw.text((10, 5), 'Stop')
        lcd.update()
        """Motor Control"""

    elif data == 'Film':
        lcd.clear()
        lcd.draw.text((10, 5), 'Film')
        lcd.update()
        file_path = '/home/robot/socket_test/webcam.jpg'
        command = ['fswebcam', '--no-banner', '--resolution', '480x480', '--save', file_path]
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

    elif data == 'Exit':
        lcd.clear()
        lcd.draw.text((10, 5), 'Exit')
        lcd.update()
        client.close()

client.close()