#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket
import subprocess

lcd = Screen()
btn = Button()
A_motor = LargeMotor('outA')
D_motor = LargeMotor('outD')

Server_Addr = ('192.168.23.', 12344)
#IPv4 IP address

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
        A_motor.run_forever(speed_sp=500)

    elif data == 'Backward':
        lcd.clear()
        lcd.draw.text((10, 5), 'Backward')
        lcd.update()
        """Motor Control"""
        A_motor.run_forever(speed_sp=-500)

    elif data == 'Left':
        lcd.clear()
        lcd.draw.text((10, 5), 'Left')
        lcd.update()
        """Motor Control"""
        D_motor.run_to_rel_pos(position_sp=-20, speed_sp=200)

    elif data == 'Right':
        lcd.clear()
        lcd.draw.text((10, 5), 'Right')
        lcd.update()
        """Motor Control"""
        D_motor.run_to_rel_pos(position_sp=20, speed_sp=200)

    elif data == 'Stop':
        lcd.clear()
        lcd.draw.text((10, 5), 'Stop')
        lcd.update()
        """Motor Control"""
        A_motor.stop()
        D_motor.stop()

    elif data == 'Film':
        lcd.clear()
        lcd.draw.text((10, 5), 'Film')
        lcd.update()
        client.send(':Film'.encode())
        
        file_path = '/home/robot/test5/webcam.jpg'
        command = ['fswebcam', '--no-banner', '--resolution', '480x480', '--save', file_path]
        subprocess.run(command)

        with open(file_path, 'rb') as file:
            file_size = len(file.read())
            client.send(str(file_size).encode())
            file.seek(0)
            while True:
                data = file.read(1024)
                if not data:
                    break
                client.send(data)

    elif data == 'Exit':
        lcd.clear()
        lcd.draw.text((10, 5), 'Exit')
        lcd.update()
        client.close()

client.close()