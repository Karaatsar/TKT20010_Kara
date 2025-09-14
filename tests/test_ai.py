from connect4.board import Board
from ai import evaluate_board, minimax

def test_ai_wins_immediately():
    board=Board()
    player=1
    for c in range(3): #kolme nappulaa peräkkäin ja neljäs vapaa
        board.make_move(c, player)
    score, move=minimax(board, depth=2, alpha=-9999,beta=9999, maximizing=True, player=player)
    assert move==3 #AI voittaa neljännellä siirrolla

