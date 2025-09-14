import pytest
from connect4.board import Board

def test_new_board_is_empty():
    board=Board()
    assert all(cell==0 for row in board.grid for cell in row)

def test_make_move_valid():
    board=Board()
    assert board.make_move(3,1)
    assert board.grid[5][3]==1

def test_cannot_play_full_column():
    board=Board()
    for _ in range(6):
        board.make_move(0,1)
    assert not board.make_move(0,-1)

def test_get_valid_moves():
    board=Board()
    moves=board.get_valid_moves()
    assert set(moves)==set(range(7))

def test_winner_horizontal():
    board=Board()
    player=1
    row=5
    for col in range(4):
        board.make_move(col, player)
    assert board.check_winner(row, 3)==player

def test_winner_vertical():
    board=Board()
    player=-1
    col=0
    last_row=None
    for _ in range(4):
        board.make_move(col, player)
        last_row=next(r for r in range(rows) if board.grid[r][col]==player)
    assert board.check_winner(last_row, col)==player

def test_winner_diagonal_right():
    board=Board()
    player=1
    moves=[(5,0), (4,1), (3,2), (2,3)]
    for r,c, in moves: 
        board.grid[r][c]=player
    last_row, last_col=moves[-1]
    assert board.check_winner(last_row, last_col)==player

def test_winner_diagonal_left():
    board=Board()
    player=-1
    moves=[(2,0), (3,1), (4,2), (5,3)]
    for r,c in moves:
        board.grid[r][c]=player
    last_row, last_col=moves[-1]
    assert board.check_winner(last_row, last_col)==player


        

