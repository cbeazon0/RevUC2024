import socketio
import threading

def receive_messages():
    while True:
        message = input()  # Assuming you want to input messages from the terminal
        if message.lower() == 'exit':
            sio.disconnect()
            break
        sio.emit('message', message)

sio = socketio.Client()

@sio.event
def connect():
    print("[CONNECTED] You are now connected to the chatroom.")

@sio.event
def message(data):
    print(data)

HOST = 'http://172.16.3.53:5000'

sio.connect(HOST)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    if message.lower() == 'exit':
        sio.disconnect()
        break
    sio.emit('message', message)