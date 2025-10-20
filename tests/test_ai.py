from connect4.board import Board
from ai import evaluate_board, minimax, find_best_move

def test_ai_wins_immediately():
    board=Board()
    player=1
    for c in range(3): #kolme nappulaa peräkkäin ja neljäs vapaa
        board.make_move(c, player)
    score, move=minimax(board, depth=2, alpha=-9999,beta=9999, maximizing=True, player=player)
    assert move==3 #AI voittaa neljännellä siirrolla

def test_heuristic_preferes_center():
    '''suosii keskimmäistä reunaan verrattuna'''
    board_center=Board()
    board_center.make_move(3,1) #täysin keskellä
    board_edge=Board()
    board_edge.make_move(0,1)   #reunassa
    center_score=evaluate_board(board_center, 1)
    edge_score=evaluate_board(board_edge, 1)
    assert center_score>edge_score

def test_ai_plays_legal():
    '''AI tekee vain laillisia siirtoja'''
    board=Board()
    move=find_best_move(board, player=-1, time_limit=1.0)
    assert move in board.get_valid_moves()

def test_ai_blocks_opponent_win():
    '''Ai estää vastustajan voiton'''
    board=Board()
    for c in range(3):
        board.make_move(c, 1) #pelaajalla on kolme peräkkäin
    best_move=find_best_move(board, player=-1, time_limit=1.0)
    assert best_move==3 

def test_minimax_symmetria():
    '''heuristiika on symmetrinen'''
    board=Board()
    board.make_move(3,1)
    score1=evaluate_board(board, 1)
    score2=evaluate_board(board, -1)
    assert score1==-score2

def test_ai_chooses_winning_over_blocking():
    '''Ai valitsee voiton estämisen sijaan'''
    board=Board()

