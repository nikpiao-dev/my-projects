from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def play_game():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Final project - Python</title>
    <link rel="stylesheet" href="static/main.css">
</head>
<body>
    <div class="app-container">
        <h1>Rock, Paper, Scissors</h1>
    </div>
</body>
</html>"""


# Possible moves
choices = ['rock', 'paper', 'scissors']

# random moves computer
bot_move = random.choice(choices)


def find_winner(user_pick):
    if user_pick == bot_move:
        return f"It's a draw!, {user_pick} = {bot_move}"
    else:
        pass

print(find_winner("paper"))