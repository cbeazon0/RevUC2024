import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from datetime import datetime
from markupsafe import Markup

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from flask_socketio import SocketIO, send

# Load environment variables from .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Configure flask for application needs
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
socketio = SocketIO(app, cors_allowed_origins = "*")

# Configure Authlib to handle applications authentication with Auth0
oauth = OAuth(app)

# Register Auth0 as the OAuth provider
oauth.register(
    "auth0",
    client_id = env.get("AUTH0_CLIENT_ID"),
    client_secret = env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs = {
        "scope": "openid profile email",
    },
    server_metadata_url = f"https://{env.get('AUTH0_DOMAIN')}/.well-known/openid-configuration",
)
    

##############
### Routes ###
##############

# Go to login route
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(redirect_uri = url_for("callback", _external = True))

# Go to callback route after login
@app.route("/callback", methods = ["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

# Go to logout route and ensure their session is completely cleared before redirecting to home route
@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + 
        env.get("AUTH0_DOMAIN") + 
        "/v2/logout?" + 
        urlencode(
            {
                "returnTo": url_for("home", _external = True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
                },
            quote_via = quote_plus,
            )
    )

# Go to learn page
@app.route("/learn")
def learn():
    return render_template("learn.html", session = session.get("user"), pretty = json.dumps(session.get("user"), indent = 4))

# Go to game page
@app.route("/game")
def game():
    return render_template("game.html", session = session.get("user"), pretty = json.dumps(session.get("user"), indent = 4))

# Go to chat page
@app.route("/chat")
def chat():
    return render_template("chat.html", session = session.get("user"), pretty = json.dumps(session.get("user"), indent = 4))

# Go to initial page
@app.route("/")
def home():
    return render_template("home.html", session = session.get("user"), pretty = json.dumps(session.get("user"), indent = 4))


#################
### Chat Page ###
#################

# Chat history list
chat_history = []

# Message handling
@socketio.on("message")
def handle_message(message):
    print("Received message:" + message)
    if message != "User connected!":
        now = datetime.now()
        timestamp = now.strftime("%H:%M:%S")
        message_with_timestamp = f"[{timestamp}]{message}"
        chat_history.append(message_with_timestamp)
        send(message_with_timestamp, broadcast = True)
        
# Event handling for new client connection
@socketio.on("connect")
def handle_connect():
    print("New client connected!")
    for message in chat_history:
        send(message)

# Event handling for client disconnection
@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected!")

# Run the application and listen for connections
if __name__ == "__main__":
    socketio.run(app, host = "localhost")