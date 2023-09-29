import socket
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from PIL import Image
import tkinter as tk

Server_Addr = ("0.0.0.0", 12344)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(Server_Addr)
server_socket.listen()

print(f"Server is listening on {Server_Addr}")

client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

window = tk.Tk()
window.title("EV3 Remote Control")
window.geometry("809x500")

STATUS_connection = tk.Label(window, text="Connected!", fg="green")
STATUS_connection.grid(row=0, column=0)

def send_command(command):
    try:
        client_socket.send(command.encode())
    except Exception as e:
        connection_status.config(text=f"Error: {str(e)}")

def Forward():
    send_command("forward")
    STATUS_signal.config(text="Forward")
    STATUS_signal.grid(row=1, column=4, columnspan=4)

def Backward():
    send_command("backward")
    STATUS_signal.config(text="Backward")
    STATUS_signal.grid(row=1, column=4, columnspan=4)

def Left():
    send_command("Left")
    STATUS_signal.config(text="Left")
    STATUS_signal.grid(row=1, column=4, columnspan=4)

def Right():
    send_command("Right")
    STATUS_signal.config(text="Right")
    STATUS_signal.grid(row=1, column=4, columnspan=4)

def Stop():
    send_command("Stop")
    STATUS_signal.config(text="Stop")
    STATUS_signal.grid(row=1, column=4, columnspan=4)

def Film():
    send_command("Film")
    STATUS_signal.config(text="Film")
    STATUS_signal.grid(row=1, column=4, columnspan=4)
    
def Exit():
    client_socket.close()
    server_socket.close()
    window.destroy()

Forward = tk.Button(window, text="Forward", command=Forward)
Forward.grid(row=1, column=1)

Backward = tk.Button(window, text="Backward", command=Backward)
Backward.grid(row=3, column=1)

Left = tk.Button(window, text="Left", command=Left)
Left.grid(row=2, column=0)

Right = tk.Button(window, text="Right", command=Right)
Right.grid(row=2, column=2)

Stop = tk.Button(window, text="Stop", command=Stop)
Stop.grid(row=2, column=1)

Film = tk.Button(window, text="Film", command=Film)
Film.grid(row=2, column=3)

ExitButton = tk.Button(window, text="Exit", command=Exit)
ExitButton.grid(row=2, column=4)

STATUS_signal = tk.Label(window, text="")
STATUS_signal.grid(row=1, column=4, columnspan=4)

window.mainloop()