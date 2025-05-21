from flask import Flask, request
import random

app = Flask(__name__)


# Possible moves
choices = ['rock', 'paper', 'scissors']

# Decide the winner between "user" and "computer"
def find_winner(user_pick):
    # random moves computer
    bot_move = random.choice(choices)
    print(f"You picked: {user_pick}")
    print(f"Computer chose: {bot_move}")

    if user_pick == bot_move:
        return "It's a draw!"
    elif user_pick == "rock" and bot_move == "scissors":
        return "You Win!"
    elif user_pick == "paper" and bot_move == "rock":
        return "You win!"
    elif user_pick == "scissors" and bot_move == "paper":
        return "You win!"
    else:
        return "You lose!"

def reset_game():
    pass

@app.route("/", methods=["GET", "POST"])
def play_game():
    # Use request method to handle GET & POST requests
    result = None
    user_pick = None
    bot_move = None
    
    if request.method == "POST":
        user_pick = request.form.get('choice')
        bot_move = random.choice(choices)
        result = find_winner(user_pick)

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
        <section class="form-section">
            <form method="POST">
                <button name="choice" value="rock"></button>
                <button name="choice" value="paper"></button>
                <button name="choice" value="scissors"></button>
            </form>
        </section>

        {% if result %}
        <section class="result">
            <p>You chose: {{ user_choice }}</p>
            <p>Computer chose: {{ computer_choice }}</p>
            <h2>{{ result }}</h2>
        </section>
    </div>
</body>
</html>"""







if __name__ == '__main__':
    app.run(debug=True)