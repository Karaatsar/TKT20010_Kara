rows=6
columns=7

class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]

    def is_valid_move(self, column: int) -> bool:
        return self.grid[0][column]==0
    
    def make_move(self, column: int, player: int) -> bool:
        if not self.is_valid_move(column):
            return False
        for row in range(rows-1, -1, -1):
            if self.grid[row][column]==0:
                self.grid[row][column]=player
                return True
        return False
    
    def get_valid_moves(self):
        return [c for c in range(columns) if self.is_valid_move(c)]
    
    def __str__(self):
        return "\n".join(" ".join(str(cell) for cell in row) for row in self.grid)
    
