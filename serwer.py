import socket
import threading

# Server configuration
HOST = '62.171.135.103'
PORT = 42068

# Create a socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# List to store all connected clients
clients = []


# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        # Send the message to everyone except the sender
        if client != client_socket:
            try:
                client.send(message)
            except:
                # If sending the message fails, remove the client
                clients.remove(client)


# Function to handle individual client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive data from the client
            message = client_socket.recv(1024)
            if not message:
                # If no data is received, the client has disconnected
                break
            # Broadcast the message to all other clients
            broadcast(message, client_socket)
        except:
            # If an error occurs, the client has disconnected
            break


# Function to accept new client connections
def accept_connections():
    while True:
        # Accept a new connection
        client, address = server.accept()
        # Add the new client to the list
        clients.append(client)
        # Print a message indicating the new connection
        print(f"Connection established from {address}")
        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client,))
        client_thread.start()


# Start listening for connections
server.listen()
print(f"Server is listening on {HOST}:{PORT}")

# Create a thread to accept new connections
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
