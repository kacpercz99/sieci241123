import socket
import threading

# Client configuration
HOST = '62.171.135.103'
PORT = 42068

# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# Function to receive and print messages from the server
def receive():
    while True:
        try:
            # Receive data from the server
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            # If an error occurs, the connection is likely closed
            print("An error occurred. Connection closed.")
            client.close()
            break


# Function to send messages to the server
def send():
    while True:
        # Get user input
        message = input()
        # Send the message to the server
        client.send(message.encode('utf-8'))


# Create threads for receiving and sending messages
receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
