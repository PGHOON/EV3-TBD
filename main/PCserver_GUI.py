import socket
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from PIL import Image, ImageTk
import tkinter as tk
import threading

Server_Addr = ("0.0.0.0", 12344)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(Server_Addr)
server_socket.listen()

print(f"Server is listening on {Server_Addr}")


client_socket = None

def update_image(image_path):
    try:
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        IMAGE.config(image=photo)
        IMAGE.image = photo
    except Exception as e:
        print(f"Error updating image: {str(e)}")

def send_command(command):
    try:
        global client_socket
        client_socket.send(command.encode())
    except Exception as e:
        STATUS_signal.config(text=f"Error: {str(e)}")

def Forward():
    send_command("Forward")
    STATUS_signal.config(text="Forward")
    STATUS_signal.grid(row=1, column=4, columnspan=4)

def Backward():
    send_command("Backward")
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


def handle_client_thread(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                print("Connection closed by client.")
                break

            if data == ':Film':
                file_size = int(client_socket.recv(1024).decode())
                with open('received_image.jpg', "wb") as file:
                    received_size = 0
                    while received_size < file_size:
                        jpg_chunk = client_socket.recv(1024)
                        if not jpg_chunk:
                            break
                        file.write(jpg_chunk)
                        received_size += len(jpg_chunk)
                update_image("received_image.jpg")

                CLASSES = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
                model = load_model('model2.h5')
                image_path = 'received_image.jpg'
                img = Image.open(image_path)
                img = img.resize((32, 32))
                img = np.array(img)
                img = np.expand_dims(img, axis=0)
                img = preprocess_input(img)

                predictions = model.predict(img)

                predicted_class_index = np.argmax(predictions, axis=1)
                predicted_class_name = CLASSES[predicted_class_index[0]]
                print("predicted: " + predicted_class_name)

                STATUS_signal.config(text=predicted_class_name)
                STATUS_signal.grid(row=1, column=4, columnspan=4)

        except ConnectionResetError:
            print("Connection closed by client.")
            break

def handle_client_connection():
    global client_socket
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")
    handle_client_thread(client_socket)

window = tk.Tk()
window.title("EV3 Remote Control")
window.geometry("645x600")

STATUS_connection = tk.Label(window, text="Connected!", fg="green")
STATUS_connection.grid(row=0, column=0)

IMAGE = tk.Label(window)
IMAGE.grid(row=4, column=0, columnspan=5)
photo = None
update_image("default.jpg")

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

client_thread = threading.Thread(target=handle_client_connection)
client_thread.start()

window.mainloop()