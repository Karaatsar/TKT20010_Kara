from board import Board, rows, cols
from ai import evaluate_board, minimax, find_best_move

def play_moves(board: Board, moves):
    for col, player in moves:
        ok= board.make_move(col, player)
        assert ok, f"sarake {col} täynnä"
    return board

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
    best_move=minimax(board, depth=2, alpha=-9999,beta=9999, maximizing=True, player=-1)
    assert best_move in board.get_valid_moves()
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
    for r in range(3):
        board.grid[r][0]=-1
    for c in range(3,6):
        board.grid[5][c]=1
    
    score, move=minimax(board, depth=2, alpha=-9999,beta=9999, maximizing=True, player=-1)
    assert move==0 #AI valitsee voittavan siirron

def test_ai_recognizes_forced_win():
    '''AI tunnistaa pakotetun voiton'''
    board=Board()
    
    board.make_move(3,1)
    score1, ai_move_1=minimax(board, depth=2, alpha=-9999,beta=9999, maximizing=True, player=-1)
    assert ai_move_1 in board.get_valid_moves()
    board.make_move(ai_move_1,-1)

    board.make_move(2,1)
    score2, ai_move_2=minimax(board, depth=2, alpha=-9999,beta=9999, maximizing=True, player=-1)
    assert ai_move_2 in board.get_valid_moves()
    board.make_move(ai_move_2,-1)


    board.make_move(4,1)
    score3, ai_move_3=minimax(board, depth=4, alpha=-9999,beta=9999, maximizing=True, player=-1)
    assert ai_move_3 in board.get_valid_moves()

    assert score3>0

def test_minimax_finds_winning_move():
    '''tämä testaa tilanteen, jossa AI:lla on varma voitto
    5 siirrolla, mutta ei nopeampaa varmaa voittoa. 
    minimaxin tulee löytää oikea siirto syvyydellä 5 ja palauttaa
    voittoa vastaava arvo.'''
    board=Board()
    player=1
    ai_player=-1
    #rakennetaan alkutilanne, jossa AI:lla on pakotettu voitto, mutta ei välitön
    moves = [
        (3, player), 
        (2, ai_player), 
        (3, player), 
        (4, ai_player), 
        (2, player), 
        (3, ai_player)
    ]
    for col, p in moves:
        board.make_move(col, p)
    # minimax löytää varman voiton vain riittävällä syvyydellä

    score, move = minimax(
        board, depth=5, alpha=-9999, beta=9999, 
        maximizing=True, player=ai_player)
    
    assert move in board.get_valid_moves()
    assert score>900 #TÄMÄ kertoo varmasta voitosta

    #tehdään AI:n siirto
    board.make_move(move, ai_player)

    #vastustaja tekee siirron, mutta ei nopeuta AI:n voittoa
    opponent_move=board.get_valid_moves()[0]
    board.make_move(opponent_move, player)

    score2, move2 = minimax(
        board, depth=5, alpha=-9999, beta=9999, 
        maximizing=True, player=ai_player)

    assert move2 in board.get_valid_moves()
    assert score2>900 #TÄMÄ kertoo varmasta voitosta


