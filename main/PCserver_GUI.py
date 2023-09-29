import socket
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from PIL import Image
import tkinter as tk

window = tk.Tk()
window.title("EV3 Remote Control")
window.geometry("809x500")

Server_Addr = ('192.168.2.2', 12344)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(Server_Addr)

server_socket.listen(1)

STATUS = tk.Label(window, text="Waiting for a connection...")
STATUS.grid(row=1, column=4, columnspan=4)

client_socket, client_address = server_socket.accept()

def send_command(command):
    try:
        client_socket.send(command.encode())
    except Exception as e:
        STATUS.config(text=f"Error: {str(e)}")
        
def Forward():
    #send_command('forward')
    STATUS.config(text="Forward")

def Backward():
    send_command('backword')
    STATUS.config(text="Backward")

def Left():
    send_command('Left')
    STATUS.config(text="Left")
    
def Right():
    send_command('Right')
    STATUS.config(text="Right")
    
def Stop():
    send_command('Stop')
    STATUS.config(text="Stop")

def Film():
    send_command('Film')
    STATUS.config(text="Film")

Forward = tk.Button(window, text="Forward", command=Forward)
Forward.grid(row=0, column=1)

Backward = tk.Button(window, text="Backward", command=Backward)
Backward.grid(row=2, column=1)

Left = tk.Button(window, text="Left", command=Left)
Left.grid(row=1, column=0)

Right = tk.Button(window, text="Right", command=Right)
Right.grid(row=1, column=2)

Stop = tk.Button(window, text="Stop", command=Stop)
Stop.grid(row=1, column=1)

Film = tk.Button(window, text="Film", command=Film)
Film.grid(row=1, column=3)

STATUS = tk.Label(window, text="")
STATUS.grid(row=1, column=4, columnspan=4)

window.mainloop()