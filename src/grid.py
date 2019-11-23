from src import Cell

class Grid(object):
    
    def __init__(self,size: int):
        self.grid = self._generate_grid(size=size)
        self.cells = []
        self.size = size

    def _generate_grid(self,size: int):
        grid = []
        for gridline in range(0,size):
            row = [None for i in range(0,size)]
            grid.append(row)
        return grid

    def set_cell(self, cell: Cell):
        position = cell.return_position()
        self.cells.append(cell)
        self.grid[position[0]][position[1]] = cell

    def return_cell(self, position_x:int, position_y:int) -> Cell:
        return [cell for cell in self.cells if cell.position() == [position_x, position_y]]
    