#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket

lcd = Screen()
btn = Button()

Server_Addr = ('169.254.153.220', 5555)

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
        try:
            file = open('watermelon.jpg', 'rb')
            data = file.read(2048)
            while data:
                client.send(data)
                data = file.read(2048)
            lcd.clear()
            lcd.draw.text((10, 5), 'Image has been sent')
            lcd.update()
        except Exception as e:
            lcd.clear()
            lcd.draw.text((10, 5), "Error")
            lcd.update()
        finally:
            file.close()

client.close()