
from src import Grid
from src import Cell

class GameOfLife():
    def __init__(self, grid: Grid):
        self.grid = grid
    

    def apply_rule_one(self, cell: Cell) -> bool:
        surrounded_alive_cells = []
        cell_positions = cell.return_position()
        x = cell_positions[0]
        y = cell_positions[1]
        allowed_positions = [ [x-1, y], [x+1, y], [x, y-1], [x, y+1], [x+1, y+1], [x-1, y-1], [x-1, y+1], [x+1, y-1] ]
        for row in range (0,self.grid.size):
            [surrounded_alive_cells.append(cell) for cell in self.grid.grid[row] if cell.live and cell.position in allowed_positions ]
        
        if  len(surrounded_alive_cells) > 3:
            cell.live = False
            return False

        return True

    def apply_rule_two(self, cell: Cell) -> bool:
        surrounded_alive_cells = []
        cell_positions = cell.return_position()
        x = cell_positions[0]
        y = cell_positions[1]
        allowed_positions = [ [x-1, y], [x+1, y], [x, y-1], [x, y+1], [x+1, y+1], [x-1, y-1], [x-1, y+1], [x+1, y-1] ]
        for row in range (0,self.grid.size):
            [surrounded_alive_cells.append(cell) for cell in self.grid.grid[row] if cell.live and cell.position in allowed_positions ]
        
        if  len(surrounded_alive_cells) < 2:
            cell.live = False
            return False

        return True

    def apply_rule_three(self, cell: Cell) -> bool:
        surrounded_alive_cells = []
        cell_positions = cell.return_position()
        x = cell_positions[0]
        y = cell_positions[1]
        allowed_positions = [ [x-1, y], [x+1, y], [x, y-1], [x, y+1], [x+1, y+1], [x-1, y-1], [x-1, y+1], [x+1, y-1] ]
        for row in range (0,self.grid.size):
            [surrounded_alive_cells.append(cell) for cell in self.grid.grid[row] if cell.live and cell.position in allowed_positions ]
        
        if  len(surrounded_alive_cells) == 3:
            cell.live = True
            return True

        return False

    def apply_rule_four(self, cell: Cell) -> bool:
        surrounded_alive_cells = []
        cell_positions = cell.return_position()
        x = cell_positions[0]
        y = cell_positions[1]
        allowed_positions = [ [x-1, y], [x+1, y], [x, y-1], [x, y+1], [x+1, y+1], [x-1, y-1], [x-1, y+1], [x+1, y-1] ]
        for row in range (0,self.grid.size):
            [surrounded_alive_cells.append(cell) for cell in self.grid.grid[row] if cell.live and cell.position in allowed_positions ]
        
        if  (len(surrounded_alive_cells) == 2 or len(surrounded_alive_cells) == 3) and Cell.live == True:
            cell.live = True
            return True

        return False

