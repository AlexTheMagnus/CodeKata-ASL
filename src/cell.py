from .life import Life
from .position import Position

class Cell(object):

    def __init__(self, live:Life, position_x: Position, position_y: Position):
        self.live = live.status
        self.position = self._set_position(position_x, position_y)

    def _set_position(self, position_x: Position, position_y: Position) -> list:
        if (position_y.pos < 0 or position_x.pos < 0):
            return False
        return [position_x.pos, position_y.pos]
    
    def return_position(self) -> tuple:
        return self.position
    
    def return_live(self) -> bool:
        return self.live