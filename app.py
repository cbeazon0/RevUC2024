from flask import Flask, render_template

app = Flask(__name__)

# Route for game page
@app.route('/')
def gamePage():
    return render_template('game.html')

# Route for chat page
@app.route('/chat')
def chatPage():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)