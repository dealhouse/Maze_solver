from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

win = Window(800, 600)

# cell1 = Cell(100, 200, 100, 200, True, True, True, True, win)
# cell2 = Cell(300, 400, 300, 400, False, True, True, True, win)
# cell3 = Cell(500, 600, 500, 600, True, False, True, True, win)
# cell4 = Cell(700, 800, 700, 800, True, True, False, True, win)
# cell1.draw(100, 200, 100, 200)
# cell2.draw(300, 400, 300, 400)
# cell3.draw(500, 600, 500, 600)
# cell4.draw(700, 800, 700, 800)
# cell1.draw_move(cell2)

# maze = Maze(10, 10, 5, 5, 50, 50, win, seed=0)
# maze = Maze(10, 10, 5, 5, 50, 50, win, seed=42)
maze = Maze(10, 10, 5, 5, 50, 50, win, seed=123)
# maze = Maze(10, 10, 5, 5, 50, 50, win, seed=999)

maze.solve()
win.wait_for_close()



