import pytest
from board import Board, rows, columns
from ai import minimax

def test_new_board_is_empty():
    '''pelilauta on tyhjä alussa'''
    board=Board()
    assert all(cell==0 for row in board.grid for cell in row)

def test_make_move_valid():
    '''laillinen siirto onnistuu'''
    board=Board()
    assert board.make_move(3,1)
    assert board.grid[rows-1][3]==1

def test_cannot_play_full_column():
    '''siirtoa EI voida tehdä täyteen sarakkeeseen'''
    board=Board()
    for _ in range(6):
        board.make_move(0,1)
    assert not board.make_move(0,-1)

def test_get_valid_moves():
    '''palauttaa oikeat lailliset siirrot'''
    board=Board()
    moves=board.get_valid_moves()
    assert set(moves)==set(range(columns))

def test_get_valid_moves_full_column():
    board = Board()
    for _ in range(rows):
        board.make_move(0,1)
    moves = board.get_valid_moves()
    assert 0 not in moves
    assert set(moves) == set(range(1, columns))

def test_winner_horizontal():
    '''vaakasuora voitto tunnistetaan'''
    board=Board()
    player=1
    row=5
    for col in range(4):
        board.make_move(col, player)
    assert board.check_winner(row, 3)==player

def test_winner_vertical():
    '''pystysuora voitto tunnistetaan'''
    board=Board()
    player=-1
    col=0
    last_row=None
    for _ in range(4):
        board.make_move(col, player)
        last_row=next(r for r in range(rows) if board.grid[r][col]==player)
    assert board.check_winner(last_row, col)==player

def test_winner_diagonal_right():
    '''diagonaalivoitto tunnistetaan alaviistoon oikealle'''
    board=Board()
    player=1
    moves=[(5,0), (4,1), (3,2), (2,3)]
    for r,c, in moves: 
        board.grid[r][c]=player
    last_row, last_col=moves[-1]
    assert board.check_winner(last_row, last_col)==player

def test_winner_diagonal_left():
    '''diagonaalivoitto tunnistetaan alaviistoon vasemmalle'''
    board=Board()
    player=-1
    moves=[(2,0), (3,1), (4,2), (5,3)]
    for r,c in moves:
        board.grid[r][c]=player
    last_row, last_col=moves[-1]
    assert board.check_winner(last_row, last_col)==player

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

        

