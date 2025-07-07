from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def startGame():
    if request.method == "POST":
        # Handle the game logic here
        choice = request.form.get("choice")
        print(f"Player chose: {choice}")
        
    return render_template("game.html", msg="Welcome to Tic Tac Toe!")