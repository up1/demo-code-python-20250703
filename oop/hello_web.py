from flask import Flask, render_template, request
from game import Game

app = Flask(__name__)
# Initialize the game
app.config['game'] = Game()

@app.route("/", methods=["GET", "POST"])
def startGame():
    if "choice" in request.form:
        request.form = request.form.to_dict()
        # Handle the game logic here
        choice = request.form.get("choice")
        print(f"Player chose: {choice}")
        app.config['game'].play(int(choice), "x")
    if "reset" in request.form:
        app.config['game'] = Game()
        app.config['game'].start()

    return render_template("game.html", msg="Welcome to Tic Tac Toe!", slots=app.config['game'].table.slots)
if __name__ == "__main__":
    app.run(debug=True, port=5000)