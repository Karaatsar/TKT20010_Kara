from connect4.board import Board, rows, columns
from ai import minimax
import math

def print_board(board: Board):
    print(board) #tulostetaan pelilauta
    print("0 1 2 3 4 5 6") #sarakkeiden numerot

def play_game():
    board=Board()
    player=1 #pelaaja aloittaa (ei tekoäly)
    while True:
        print_board(board)
        if player==1:
            #pelaajan vuoro
            move=int(input("pelaaja: valitse sarake (0-6):"))
            if not board.make_move(move, player):
                print("virheellinen siirto, yritä uudelleen")
                continue
        else:
            #tekoälyn vuoro
            print("tekoäly miettii...")
            _, move= minimax(board, depth=4, alpha=-9999, beta=9999, 
                            maximizing=True, player=player)
            if move is None:
                print("tasapeli!!")
                break
            board.make_move(move, player)
            print(f"tekoäly valitsi sarakeen {move}")
        
        for r in range(rows):
            for c in range(columns):
                winner=board.check_winner(r,c)
                if winner:
                    print_board(board)
                    if winner==1:
                        print("sinä voitit!")
                    else:
                        print("tekoäly voitti :(")
                    return
        
        player=-player #vaihdetaan pelaajaa

if __name__=="__main__":
    play_game()
            
