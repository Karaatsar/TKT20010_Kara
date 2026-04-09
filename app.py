from flask import Flask, render_template, jsonify, request
from board import Board, rows, cols
from ai import find_best_move, minimax

app = Flask(__name__, static_folder='static', template_folder='templates')

# Simple global game state (single-session)
game = {
    'board': Board(),
    'current_player': 1,  # 1 = human, -1 = AI
    'winner': None,
}


def serialize_board(board: Board):
    return board.grid


def check_for_winner(board: Board):
    for r in range(rows):
        for c in range(cols):
            w = board.check_winner(r, c)
            if w:
                return w
    # draw?
    if not board.get_valid_moves():
        return 0
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/state')
def state():
    return jsonify({
        'grid': serialize_board(game['board']),
        'current_player': game['current_player'],
        'winner': game['winner'],
        'valid_moves': game['board'].get_valid_moves(),
    })


@app.route('/new', methods=['POST'])
def new_game():
    game['board'] = Board()
    game['current_player'] = 1
    game['winner'] = None
    return jsonify({'ok': True})


@app.route('/move', methods=['POST'])
def move():
    if game['winner'] is not None:
        return jsonify({'ok': False, 'error': 'game over', 'winner': game['winner']}), 400

    data = request.get_json() or {}
    col = data.get('column')
    if col is None or not isinstance(col, int) or not (0 <= col < cols):
        return jsonify({'ok': False, 'error': 'invalid column'}), 400

    # player's move (human is player 1)
    if not game['board'].is_valid_move(col):
        return jsonify({'ok': False, 'error': 'column full'}), 400

    last_row = game['board'].make_move(col, 1)
    game['current_player'] = -1
    game['winner'] = check_for_winner(game['board'])
    if game['winner'] is not None:
        return jsonify({'ok': True, 'grid': serialize_board(game['board']), 'winner': game['winner']})

    # AI's turn: use find_best_move (with small time limit) and apply
    ai_move = find_best_move(game['board'], player=-1, time_limit=1.0)
    if ai_move is None:
        # no move -> draw
        game['winner'] = 0
        return jsonify({'ok': True, 'grid': serialize_board(game['board']), 'winner': game['winner']})

    game['board'].make_move(ai_move, -1)
    game['current_player'] = 1
    game['winner'] = check_for_winner(game['board'])

    return jsonify({'ok': True, 'grid': serialize_board(game['board']), 'ai_move': ai_move, 'winner': game['winner']})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
