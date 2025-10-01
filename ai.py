'''tekoälyn logiikkaa connect4 peliin käyttämällä minimax ja alpha-beta karsintaa'''
import math
import time
from connect4.board import Board, rows, columns

table={}
def board_key(board: Board):
    #luodaan pelilaudasta avain sanakirjaa varten
    return tuple(tuple(row) for row in board.grid)

def evaluate_window(window, player: int) -> int:
    #arvioidaan neljän mittaisen ikkunan tilanne
    score=0
    opponent=-player
    if window.count(player)==4: 
        score+=100
    elif window.count(player)==3 and window.count(0)==1:
        score+=10
    elif window.count(player)==2 and window.count(0)==2:
        score+=5
    if window.count(opponent)==3 and window.count(0)==1:
        score-=80 #estetään vastustajan voitto
    return score

def evaluate_board(board: Board, player: int) -> int:
    #arvioidaan pelilauta
    score = 0
    center_col=columns//2
    center_array = [board.grid[r][center_col] for r in range(rows)] #keskimmäisen sarakkeen suosiminen
    score+=center_array.count(player)*3

    for r in range(rows): #vaakasuorat ikkunat
        for c in range(columns-3):
            window=[board.grid[r][c+i] for i in range(4)]
            score+=evaluate_window(window, player)
    
    for c in range(columns): #pystysuorat ikkunat
        for r in range(rows-3):
            window=[board.grid[r+i][c] for i in range(4)]
            score+=evaluate_window(window, player)

    for r in range(rows-3): #diagonaalit alas oikealle
        for c in range(columns-3):
            window=[board.grid[r+i][c+i] for i in range(4)]
            score+=evaluate_window(window, player)

    for r in range(3, rows): #diagonaalit alas vasemmalle
        for c in range(3, columns):
            window=[board.grid[r-i][c-i] for i in range(4)]
            score+=evaluate_window(window, player)
    
    return score


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

        key = board_key(board)
        if key in table:
            first=[table[key]]
            others=[m for m in valid_moves if m!=table[key]]
            valid_moves=first+others

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
        if best_move is not None:
            table[key]=best_move
        return value, best_move
    
    else: #min!
        value=math.inf
        best_move=None
        for move in valid_moves:
            new_board=Board()
            new_board.grid=[row[:] for row in board.grid]
            new_board.make_move(move, opponent)
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
    
def find_best_move(board:Board, player: int, time_limit:float=2.0):
    #etsitään paras siirto aikarajan puitteissa
    start_time=time.time()
    best_move=None
    depth=1

    while True:
        if time.time()-start_time>time_limit:
            break
        score, move=minimax(board, depth, -math.inf, math.inf, True, player)
        if move is not None:
            best_move=move
        depth+=1
    return best_move