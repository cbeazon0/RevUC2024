import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except ConnectionResetError:
            print("[ERROR] Connection with the server has been reset.")
            break

HOST = '172.16.3.53'
PORT = 55555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("[CONNECTED] You are now connected to the chatroom.")

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    message = input()
    if message.lower() == 'exit':
        client_socket.close()
        break
    client_socket.send(message.encode("utf-8"))