#!/usr/bin/env python3
from ev3dev.ev3 import *
import socket

lcd = Screen()

Server_Addr = ('169.254.252.180', 5555)

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(Server_Addr)
lcd.clear()
lcd.draw.text((10, 5), 'Connecting to Server ...')
lcd.update()

while True:
    lcd.clear()
    lcd.draw.text((10, 5), 'Connected!!!')
    lcd.update()
    client_socket.send('...'.encode())

client_socket.close()
