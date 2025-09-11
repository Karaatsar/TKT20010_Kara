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
