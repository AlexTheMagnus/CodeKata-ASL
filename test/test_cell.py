import unittest
from src import Cell
from src import Life
from src import Position

class CellGeneration(unittest.TestCase):

    def test_generate_live_cell(self):
        state = Life(True)
        posX = Position(0)
        posY = Position(0)
        cell = Cell(live=state,position_x= posX, position_y = posY)
        self.assertEqual(True, cell.live)
    
    def test_generate_dead_cell(self):
        state = Life(False)
        posX = Position(0)
        posY = Position(0)
        cell = Cell(live=state,position_x= posX, position_y = posY)
        self.assertEqual(False, cell.live)
    
    def test_assign_wrong_coordinates(self):
        state = Life(False)
        posX = Position(-12)
        posY = Position(2)
        cell = Cell(live=state,position_x= posX, position_y = posY)
        self.assertEqual(False, cell.return_position())
    
    def test_assign_correct_coordinates(self):
        state = Life(False)
        posX = Position(12)
        posY = Position(2)
        cell = Cell(live=state,position_x= posX, position_y = posY)
        self.assertEqual([12,2], cell.return_position())
    



if __name__ == '__main__':
    unittest.main()