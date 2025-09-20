import math
from connect4.board import Board, rows, columns

def evaluate_board(board: Board, player: int) -> int:
    opponent=-player
    score=0
    for r in range(rows):
        for c in range(columns):
            winner=board.check_winner(r,c)
            if winner==player:
                return 1000 #+1000 jos pelaaja voittaa
            else:
                return -1000 #-100 jos vastustaja (opponent) voittaa
    center_col=columns//2
    center_count=sum(row(center_col)==player for row in board.grid)
    score+=center_count*3
    return score #tekoäly suosii keskimmäistä saraketta

def minimax(board:Board, depth:int, alpha:float, beta:float, maximizing:bool, 
            player:int) ->tuple[int, int | None]: #alpha_beta karsinnalla
    
    opponent=-player
    valid_moves=board.get_valid_moves()

    if depth==0 or not valid_moves:
        score=evaluate_board(board, player)
        return score, None
    
    if maximizing: #max!
        value=-math.inf
        best_move=None
        for move in valid_moves:
            new_board=Board()
            new_board.grid=[row[:] for row in board.grid]
            new_board.make_move(move, player)
            last_row=next(r for r in range(rows) if new_board.grid[r][move]!=0)
            if new_board.check_winner(last_row, move)==player:
                return 1000, move #tarkistetaan tuliko voitto heti
            new_score,_=minimax(new_board, depth-1, alpha, beta, False, player)
            if new_score>value:
                value=new_score
                best_move=move
            alpha=max(alpha, value)
            if alpha>=beta:
                break
        return value, best_move
    
    else: #min!
        value=math.inf
        best_move=None
        for move in valid_moves:
            new_board=Board()
            new_board.grid=[row[:] for row in board.grid]
            new_board.make_move(move, player)
            last_row=next(r for r in range(rows) if new_board.grid[r][move]!=0)
            if new_board.check_winner(last_row, move)==player:
                return 1000, move #tarkistetaan tuliko voitto heti
            new_score,_=minimax(new_board, depth-1, alpha, beta, True, player)
            if new_score<value:
                value=new_score
                best_move=move
            beta=min(beta, value)
            if beta<=alpha:
                break
        return value, best_move
    

    


    

