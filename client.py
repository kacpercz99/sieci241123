import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('62.171.135.103', 42068)
client_socket.connect(server_address)
nick = input("Podaj nick: ")
try:
    message = ''
    while True:
        message = input()
        message = f"{nick}: {message}"
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024)
        print(data.decode('utf-8'))

except KeyboardInterrupt:
    print("\nZamykanie klienta...")
finally:
    client_socket.close()
