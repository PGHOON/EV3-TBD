import socket

HOST = '0.0.0.0'    #or Replace "0.0.0.0" with the IP address that appears in the top left corner of the EV3 brick's screen.
                    #0.0.0.0 will listen every port available
PORT = 5555

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            print("Connection closed by client.")
            break

        # Connection Cheking
        if data == '...':
            print("...")

    except ConnectionResetError:
        print("Connection closed by client.")
        break
    
client_socket.close()
server_socket.close()

