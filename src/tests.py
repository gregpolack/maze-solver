import unittest

from graphics import Window
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_maze_create_bigger_cells(self):
        num_cols = 13
        num_rows = 19

        m1 = Maze(50, 50, num_rows, num_cols, 50, 50)

        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )

    def test_entrance(self):
        num_cols = 5
        num_rows = 5

        m1 = Maze(50, 50, num_rows, num_cols, 50, 50)
        m1._break_entrance_and_exit()

        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False 
        )

    def test_exit(self):
        num_cols = 5
        num_rows = 5

        m1 = Maze(50, 50, num_rows, num_cols, 50, 50)
        m1._break_entrance_and_exit()

        self.assertEqual(
            m1._cells[-1][-1].has_bot_wall,
            False
        )
    
    def test_break_walls_r(self):
        num_cols = 10
        num_rows = 10

        m1 = Maze(50, 50, num_rows, num_cols, 50, 50)
        m1._break_entrance_and_exit()
        
        self.assertIsNone(m1._break_walls_r(0, 0))

    def test_reset_cells_visited(self):
        
        num_cols = 5
        num_rows = 5

        m1 = Maze(50, 50, num_rows, num_cols, 50, 50)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()

        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)
                
if __name__ == "__main__":
    unittest.main()