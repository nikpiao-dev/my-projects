from flask import Flask, render_template, request
import random

app = Flask(__name__)


# Possible moves
choices = ['rock', 'paper', 'scissors']

# Decide the winner between "user" and "computer"
def find_winner(user_pick, bot_move):
    
    # print the result:
    print(f"You picked: {user_pick}")
    print(f"Computer chose: {bot_move}")

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

# Pick a color class based on whether you won, lost, or tied.
def pick_result_color(result_text):
    if "win" in result_text.lower():
        return "win"
    elif "lose" in result_text.lower():
        return "lose"
    else:
        return "draw"

# Use request method to handle GET & POST requests
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
        color = pick_result_color(result)

    return render_template("index.html", user_pick=user_pick, bot_move=bot_move, result=result, color=color)







if __name__ == '__main__':
    app.run(debug=True)