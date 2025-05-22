from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Available moves for the game
choices = ['rock', 'paper', 'scissors']

# Determine the outcome of the game based on user and computer choices
def find_winner(user_pick, bot_move):
    
    if user_pick == bot_move:
        return "It's a draw!"
    elif user_pick == "rock" and bot_move == "scissors":
        return "You win!"
    elif user_pick == "paper" and bot_move == "rock":
        return "You win!"
    elif user_pick == "scissors" and bot_move == "paper":
        return "You win!"
    else:
        return "You lose!"

# Pick a CSS class so the result text can be styled (green = win, red = lose, and yellow = draw)
def result_color(result_text):
    if "win" in result_text.lower():
        return "win"
    elif "lose" in result_text.lower():
        return "lose"
    else:
        return "draw"

# Main route to shows the game and handles the play
@app.route("/", methods=["GET", "POST"])
def play_game():
    result = None
    user_pick = None
    bot_move = None
    color = None
    
    if request.method == "POST":
        user_pick = request.form.get('choice')
        bot_move = random.choice(choices)
        result = find_winner(user_pick, bot_move)
        color = result_color(result)

    # Show the page with all the info
    return render_template("index.html", user_pick=user_pick, bot_move=bot_move, result=result, color=color)

if __name__ == '__main__':
    app.run(debug=True)
