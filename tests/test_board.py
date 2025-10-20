import pytest
from connect4.board import Board, rows, columns

def test_new_board_is_empty():
    '''pelilauta on tyhjä alussa'''
    board=Board()
    assert all(cell==0 for row in board.grid for cell in row)

def test_make_move_valid():
    '''laillinen siirto onnistuu'''
    board=Board()
    assert board.make_move(3,1)
    assert board.grid[5][3]==1

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
    assert set(moves)==set(range(7))

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


        

