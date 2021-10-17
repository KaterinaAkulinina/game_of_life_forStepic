from flask import Flask
from flask import render_template
from game_of_life import GameOfLife

app = Flask(__name__)

@app.route('/')
def index():
    GameOfLife(10, 10)
    return render_template('index.html')

@app.route('/live')
def live():
    game = GameOfLife()
    if game.nw > 0: game.form_new_generation()
    game.nw += 1
    return render_template('live.html', game=game)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)