rows=6
cols=7
columns = cols

class Board:
    '''luokka, joka mallintaa connect4 pelilautaa'''
    def __init__(self):
        '''tyhjä pelilauta, jossa 0=tyhjä, 1=pelaaja, -1=tekoäly'''
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def _apply_gravity(self, column: int) -> None:
        '''pudottaa sarakkeen pelinappulat alimpaan mahdolliseen kohtaan'''
        tokens=[self.grid[r][column] for r in range(rows-1, -1, -1) if self.grid[r][column]!=0]
        idx=0
        for r in range(rows-1, -1, -1):
            if idx < len(tokens):
                self.grid[r][column]=tokens[idx]
                idx+=1
            else:
                self.grid[r][column]=0

    def is_valid_move(self, column: int) -> bool:
        '''tarkistaa onko siirto mahdollinen
        palauttaa True jos siirto on mahdollinen, muuten False'''
        return any(self.grid[r][column]==0 for r in range(rows))
    
    def make_move(self, column: int, player: int) -> int | bool:
        '''tekee pelaajan siirron sarakkeeseen,
        palauttaa rivin indeksin jos siirto onnistui, muuten False'''
        self._apply_gravity(column)
        if not self.is_valid_move(column):
            return False
        # etsitään alin tyhjä rivi sarakkeessa
        for row in range(rows-1, -1, -1):
            if self.grid[row][column]==0:
                self.grid[row][column]=player
                return row
        return False
    
    def get_valid_moves(self):
        '''palauttaa listan sarakkeista, joihin voi tehdä siirron,
        keskisaraketta suosien'''
        center = cols//2
        return sorted([c for c in range(cols) if self.is_valid_move(c)], 
                      key=lambda c: abs(c-center))
        
    def copy(self):
        new_board = Board()
        new_board.grid = [row[:] for row in self.grid]
        return new_board

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
            while 0<=r<rows and 0<=c<cols and self.grid[r][c]==player:
                count+=1
                r+=dr
                c+=dc
            r, c = last_row-dr, last_col-dc
            while 0<=r<rows and 0<=c<cols and self.grid[r][c]==player:
                count+=1
                r-=dr
                c-=dc
            if count>=4:
                return player
        return None
    
            
