from cell import Cell
import time
import random
class Maze:
    def __init__(self, x1, y1, 
                num_rows, num_cols, 
                cell_size_x, cell_size_y, 
                win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        

    def _create_cells(self):
        self.cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                x1 = self.x1 + j * self.cell_size_x
                x2 = self.x1 + (j + 1) * self.cell_size_x
                y1 = self.y1 + i * self.cell_size_y
                y2 = self.y1 + (i + 1) * self.cell_size_y
                cell = Cell(x1, x2, y1, y2, True, True, True, True, self.win)
                column.append(cell)
            self.cells.append(column)
        
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        cell = self.cells[i][j]
        cell.draw()
        self._animate()
        
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        
    def _break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            possible_moves = []
            if i > 0 and not self.cells[i - 1][j].visited:
                possible_moves.append((i-1, j, "up"))
            if j > 0 and not self.cells[i][j - 1].visited:
                possible_moves.append((i, j-1, "left"))
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                possible_moves.append((i+1, j, "down"))
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                possible_moves.append((i, j+1, "right"))
            if len(possible_moves) == 0:
                    return
            else:
                move = random.choice(possible_moves)
                if move[2] == "up":
                    self.cells[i][j].has_top_wall = False
                    self.cells[i-1][j].has_bottom_wall = False
                elif move[2] == "left":
                    self.cells[i][j].has_left_wall = False
                    self.cells[i][j-1].has_right_wall = False
                elif move[2] == "down":
                    self.cells[i][j].has_bottom_wall = False
                    self.cells[i+1][j].has_top_wall = False
                elif move[2] == "right":
                    self.cells[i][j].has_right_wall = False
                    self.cells[i][j+1].has_left_wall = False
                self._break_walls_r(move[0], move[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.cells[i][j].visited = False

    def solve(self):
        solved = False
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                solved = self._solve_r(i, j)
        
        return solved

    def _solve_r(self, i, j):
        self._animate()
        self.cells[i][j].visited = True
        if self.cells[self.num_cols - 1][self.num_rows - 1].visited:
            return True
        else:
            if i > 0 and not self.cells[i - 1][j].visited and not self.cells[i][j].has_top_wall:
                self.cells[i][j].draw_move(self.cells[i - 1][j])
                if self._solve_r(i - 1, j):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i - 1][j], undo=True)
            if j > 0 and not self.cells[i][j - 1].visited and not self.cells[i][j].has_left_wall:
                self.cells[i][j].draw_move(self.cells[i][j - 1])
                if self._solve_r(i, j - 1):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j - 1], undo=True)
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited and not self.cells[i][j].has_bottom_wall:
                self.cells[i][j].draw_move(self.cells[i + 1][j])
                if self._solve_r(i + 1, j):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i + 1][j], undo=True)
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited and not self.cells[i][j].has_right_wall:
                self.cells[i][j].draw_move(self.cells[i][j + 1])
                if self._solve_r(i, j + 1):
                    return True
                else:
                    self.cells[i][j].draw_move(self.cells[i][j + 1], undo=True)
            else:
                return False
        
