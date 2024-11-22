import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    def test_maze_create_cell_2(self):
        num_cols = 30
        num_rows = 20
        m1 = Maze(10, 10, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )
    
    def test_maze_create_cell_3(self):
        num_cols = 40
        num_rows = 40
        m1 = Maze(50, 50, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 2
        num_rows = 2
        maze = Maze(10, 10, num_rows, num_cols, 20, 20)

        maze._break_entrance_and_exit()

        self.assertFalse(maze.cells[0][0].has_top_wall)
        self.assertFalse(maze.cells[num_cols - 1][num_rows - 1].has_bottom_wall)

    def test_visited_after_break(self):
        maze = Maze(10, 10, 10, 10, 10, 10)
        for i in range(10):
            for j in range(10):
                self.assertFalse(maze.cells[i][j].visited)

if __name__ == '__main__':
    unittest.main()