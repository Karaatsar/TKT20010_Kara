''' connect4-pelin pääohjelma. tässä tiedostossa moduuli käynnistää
    pelin, jossa pelaaja pelaa tekoälyä vastaan. peli pelataan 6x7
    ruudukolla, ja voittaja on se joka saa neljä peräkkäin joko
    vaakasuoraan, pystysuoraan tai vinottain.'''

from board import Board, rows, columns
from ai import minimax


def print_board(board: Board):
    '''tulostaa pelilaudan ja sarakkeiden numerot'''
    print(board) 
    print("1 2 3 4 5 6 7") 

def play_game():
    '''käynnistää pelin tekoälyä vastaan'''
    board = Board()
    player = 1 #pelaaja aloittaa (ei tekoäly)
    while True:
        print_board(board)
        if player == 1:
            #pelaajan vuoro
            try:
                move=int(input("pelaaja: valitse sarake (1-7):")) -1
            except ValueError:
                print("anna numero väliltä 1-7.")
                continue
            
            if move not in range(columns):
                print("virheellinen sarake. valitse 1-7.")
                continue
            
            if not board.make_move(move,player):
                print("sarake on täynnä, yritä toista")
                continue
        else:
            #tekoälyn vuoro
            print("tekoäly miettii...")
            _, move = minimax(board, depth=4, alpha=-9999, beta=9999, 
                            maximizing=True, player=player)
            
            if move is None:
                print("tasapeli!!")
                break

            board.make_move(move, player)
            print(f"tekoäly valitsi sarakeen {move +1}")
        
        #tarkistetaan voitto
        for r in range(rows):
            for c in range(columns):
                winner = board.check_winner(r, c)
                if winner:
                    print_board(board)
                    if winner == 1:
                        print("sinä voitit!")
                    else:
                        print("tekoäly voitti :(")
                    return
        
        player=-player #vaihdetaan pelaajaa

if __name__=="__main__":
    play_game()
            
