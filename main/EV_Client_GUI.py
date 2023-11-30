#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket
import subprocess
import os

lcd = Screen()
btn = Button()
A_motor = LargeMotor('outA')
C_motor = LargeMotor('outC')
B_motor = LargeMotor('outB')
D_motor = LargeMotor('outD')

Server_Addr = ('192.168.23.53', 12344)
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
        A_motor.run_forever(speed_sp=-500)
        C_motor.run_forever(speed_sp=-500)
        B_motor.run_forever(speed_sp=500)
        D_motor.run_forever(speed_sp=500)

    elif data == 'Backward':
        lcd.clear()
        lcd.draw.text((10, 5), 'Backward')
        lcd.update()
        """Motor Control"""
        A_motor.run_forever(speed_sp=500)
        C_motor.run_forever(speed_sp=500)
        B_motor.run_forever(speed_sp=-500)
        D_motor.run_forever(speed_sp=-500)

    elif data == 'Left':
        lcd.clear()
        lcd.draw.text((10, 5), 'Left')
        lcd.update()
        """Motor Control"""
        A_motor.run_forever(speed_sp=-500)
        C_motor.run_forever(speed_sp=500)
        B_motor.run_forever(speed_sp=500)
        D_motor.run_forever(speed_sp=-500)

    elif data == 'Right':
        lcd.clear()
        lcd.draw.text((10, 5), 'Right')
        lcd.update()
        """Motor Control"""
        A_motor.run_forever(speed_sp=500)
        C_motor.run_forever(speed_sp=-500)
        B_motor.run_forever(speed_sp=-500)
        D_motor.run_forever(speed_sp=500)

    elif data == 'Stop':
        lcd.clear()
        lcd.draw.text((10, 5), 'Stop')
        lcd.update()
        """Motor Control"""
        A_motor.stop()
        B_motor.stop()
        C_motor.stop()
        D_motor.stop()

    elif data == 'Film':
        lcd.clear()
        lcd.draw.text((10, 5), 'Film')
        lcd.update()
        client.send(':Film'.encode())
        
        file_path = '/home/robot/final3/webcam.jpg'
        command = ['fswebcam', '--no-banner', '--resolution', '480x480', '--save', file_path]
        subprocess.run(command)

        with open(file_path, 'rb') as file:
            file_data = file.read()
            file_size = len(file_data)
            client.send(str(file_size).encode())
            client.sendall(file_data)
        
    elif data == 'Exit':
        lcd.clear()
        lcd.draw.text((10, 5), 'Exit')
        lcd.update()
        client.close()