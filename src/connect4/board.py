rows=6
columns=7

class Board:
    '''luokka, joka mallintaa connect4 pelilautaa'''
    def __init__(self):
        '''tyhjä pelilauta, jossa 0=tyhjä, 1=pelaaja, -1=tekoäly'''
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]

    def is_valid_move(self, column: int) -> bool:
        '''tarkistaa onko siirto mahdollinen
        palauttaa True jos siirto on mahdollinen, muuten False'''
        return self.grid[0][column]==0
    
    def make_move(self, column: int, player: int) -> bool:
        '''tekee pelaajan siirron sarakkeeseen, 
        palauttaa True jos siirto onnistui, muuten False'''
        if not self.is_valid_move(column):
            return False
        # etsitään alin tyhjä rivi sarakkeessa
        for row in range(rows-1, -1, -1):
            if self.grid[row][column]==0:
                self.grid[row][column]=player
                return True
        return False
    
    def get_valid_moves(self):
        '''palauttaa listan sarakkeista, joihin voi tehdä siirron,
        keskisaraketta suosien'''
        center = columns//2
        return sorted([c for c in range(columns) if self.grid[0][c]==0], 
                      key=lambda c: abs(c-center))
        
    
    def __str__(self):
        '''palauttaa pelilaudan merkkijonona'''
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)
    
    def check_winner(self, last_row: int, last_col: int) -> int | None:
        '''tarkistaa, onko pelaaja voittanut, 
        palauttaa pelaajan numeron (1 tai -1), jos on voittanut, muuten None'''
        player=self.grid[last_row][last_col]
        if player==0: 
            return None
        directions=[(1,0), (0,1), (1,1), (1,-1)]
        for dr, dc in directions: 
            count=1
            r, c = last_row+dr, last_col+dc
            while 0<=r<rows and 0<=c<columns and self.grid[r][c]==player:
                count+=1
                r+=dr
                c+=dc
            r, c = last_row-dr, last_col-dc
            while 0<=r<rows and 0<=c<columns and self.grid[r][c]==player:
                count+=1
                r-=dr
                c-=dc
            if count>=4:
                return player
        return None
    
            
