import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

# Load environment variables from .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)
    
# Configure flask for application needs
app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# Configure Authlib to handle applications authentication with Auth0
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id = env.get("AUTH0_CLIENT_ID"),
    client_secret = env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs = {
        "scope": "openid profile email",
    },
    server_metadata_url = f"https://{env.get('AUTH0_DOMAIN')}/.well-known/openid-configuration",
)

# Setting up routes

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
    
# Go to home route
@app.route("/")
def home():
    return render_template("home.html", session = session.get("user"), pretty = json.dumps(session.get("user"), indent = 4))

# Run the application and listen for connections
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = env.get("PORT", 5000))