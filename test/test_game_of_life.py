import unittest
from src.game import GameOfLife
from src import Grid
from src import Cell
from src import Life
from src import Position


class TestGameOfLife(unittest.TestCase):


    def test_condition_one(self):
        test_grid = Grid(size=4)
        game = GameOfLife(grid=test_grid)
        for x in range(0,4):
            [test_grid.set_cell(Cell(live=Life(status=True), position_x=Position(x), position_y=Position(y))) for y in range(0,4)]
        self.assertEqual(False, game.apply_rule_one(Cell(live=Life(status=True), position_x=Position(2), position_y=Position(2))))


    def test_condition_two(self):
        test_grid = Grid(size=4)
        game = GameOfLife(grid=test_grid)
        for x in range(0,4):
            [test_grid.set_cell(Cell(live=Life(status=True), position_x=Position(x), position_y=Position(y))) for y in range(0,4)]

        self.assertEqual(True, game.apply_rule_two(Cell(live=Life(status=True), position_x=Position(2), position_y=Position(2))))

    def test_condition_three(self):
        test_grid = Grid(size=4)
        game = GameOfLife(grid=test_grid)
        for x in range(0,4):
            [test_grid.set_cell(Cell(live=Life(status=True), position_x=Position(x), position_y=Position(y))) for y in range(0,4)]

        self.assertEqual(False, game.apply_rule_three(Cell(live=Life(status=True), position_x=Position(2), position_y=Position(2))))


    def apply_rule_fourth(self):
        test_grid = Grid(size=4)
        game = GameOfLife(grid=test_grid)
        for x in range(0,4):
            [test_grid.set_cell(Cell(live=Life(status=False), position_x=Position(x), position_y=Position(y))) for y in range(0,4)]
        for x in range(0,1):
            [test_grid.set_cell(Cell(live=Life(status=True), position_x=Position(x), position_y=Position(y))) for y in range(0,4)]
        self.assertEqual(False, game.apply_rule_four(Cell(live=Life(status=True), position_x=Position(1), position_y=Position(1))))  


if __name__ == '__main__':
    unittest.main()