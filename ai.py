'''tekoälyn logiikkaa connect4 peliin käyttämällä minimax ja alpha-beta karsintaa
   Sisältää arviointifunktion, minimax-algoritmin ja hajautustaulun siirtojen järjes-
   tämisen tehostamiseksi.'''
import math
import time
from board import Board, rows, cols

# hajautustaulu, joka tallentaa aiemmin tutkittujen pelitilanteiden parhaiten siirtojen tallentamiseen
table={}

def board_key(board: Board):
    '''luodaan pelilaudasta avain sanakirjaa varten'''
    return tuple(tuple(row) for row in board.grid)

def evaluate_window(window, player):
    '''arvioidaan 4-ruudun ikkuna pelaajan kannalta'''
    opponent=-player
    score=0

    player_count=window.count(player)
    opponent_count=window.count(opponent)
    empty_count=window.count(0)

    #nämä pelaajan eduksi
    if player_count==3 and empty_count==1:
        score+=5
    elif player_count==2 and empty_count==2:
        score+=2
    
    #nämä vastustajan eduksi (niin sanottu symmetrinen miinus)
    if opponent_count==3 and empty_count==1:
        score-=5
    elif opponent_count==2 and empty_count==2:
        score-=2
    
    return score
    

def evaluate_board(board: Board, player: int) -> int:
    '''arvioidaan pelilauta. painottaa keskisaraketta ja etsii
    4-ruutuisia "ikkunoita"'''
    score = 0
    center_col=cols//2
    center_array = [board.grid[r][center_col] for r in range(rows)] #keskimmäisen sarakkeen suosiminen
    score+=center_array.count(player)*3 #tässä keskisarakkeen painotus

    for r in range(rows): #vaakasuorat ikkunat
        for c in range(cols-3):
            window=[board.grid[r][c+i] for i in range(4)]
            score+=evaluate_window(window, player)
    
    for c in range(cols): #pystysuorat ikkunat
        for r in range(rows-3):
            window=[board.grid[r+i][c] for i in range(4)]
            score+=evaluate_window(window, player)

    for r in range(rows-3): #diagonaalit alas oikealle
        for c in range(cols-3):
            window=[board.grid[r+i][c+i] for i in range(4)]
            score+=evaluate_window(window, player)

    for r in range(3, rows): #diagonaalit alas vasemmalle
        for c in range(3, cols):
            window=[board.grid[r-i][c-i] for i in range(4)]
            score+=evaluate_window(window, player)
    
    return score


def minimax(board:Board, depth:int, alpha:float, beta:float, maximizing:bool,
            player:int) ->tuple[int, int | None]: 
    '''minimax-algoritmi alpha-beta karsinnalla.'''
    
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
            
            last_row=new_board.make_move(move, player)
            if last_row is False:
                continue
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
            
            last_row=new_board.make_move(move, opponent)
            if last_row is False:
                continue
            if new_board.check_winner(last_row, move)==opponent:
                return -1000, move
            new_score,_=minimax(new_board, depth-1, alpha, beta, True, player)
            if new_score<value:
                value=new_score
                best_move=move
            beta=min(beta, value)
            if beta<=alpha:
                break
        return value, best_move
    
def find_best_move(board:Board, player: int, time_limit:float=2.0):
    '''etsitään paras siirto aikarajan puitteissa'''
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