from flask import Flask, render_template
from flask_socketio import SocketIO, emit

import secrets

secret_key = secrets.token_hex(32)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
socketio = SocketIO(app)

# Route for the chat page
@app.route('/chat')
def chat():
    return render_template('chat.html')

# WebSocket event handler for receiving and broadcasting messages
@socketio.on('message')
def handle_message(message):
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host = "0.0.0.0", port = 5000)