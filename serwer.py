import threading
import socket

HOST = 'localhost'
PORT = 42068

clients = []


def broadcast(message, sender_socket):
    for client in clients:
        try:
            client.send(message)
        except socket.error:
            print(f"Client {client.getpeername()} disconnected")
            clients.remove(client)


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            broadcast(message, client_socket)
        except socket.error:
            clients.remove(client_socket)
            break
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"Server is listening on port {HOST}:{PORT}")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Client {client_address} connected")
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
