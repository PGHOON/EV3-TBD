#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket

lcd = Screen()
btn = Button()

Server_Addr = ('169.254.244.189', 5555)

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

        with open('watermelon.jpg', 'rb') as file:
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