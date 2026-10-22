
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "tic-tac-toe-local-dev-key"


WINNING_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


def reset_game():
    session["board"] = [""] * 9
    session["current_player"] = "X"
    session["winner"] = None
    session["draw"] = False


def get_winner(board):
    for a, b, c in WINNING_COMBINATIONS:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


@app.route("/", methods=["GET", "POST"])
def index():
    if "board" not in session:
        reset_game()

    if request.method == "POST":
        if request.form.get("action") == "reset":
            reset_game()
            return redirect(url_for("index"))

        board = session["board"]

        if not session["winner"] and not session["draw"]:
            try:
                position = int(request.form.get("position", -1))
            except (ValueError, TypeError):
                position = -1

            if 0 <= position < 9 and board[position] == "":
                player = session["current_player"]
                board[position] = player

                winner = get_winner(board)
                session["board"] = board

                if winner:
                    session["winner"] = winner
                elif all(board):
                    session["draw"] = True
                else:
                    session["current_player"] = (
                        "O" if player == "X" else "X"
                    )

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        board=session["board"],
        current_player=session["current_player"],
        winner=session["winner"],
        draw=session["draw"]
    )


if __name__ == "__main__":
    app.run(debug=True)
