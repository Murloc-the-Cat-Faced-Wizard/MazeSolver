import time
import random
from Cell import Cell

class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_x_len, cell_y_len=None, win=None, seed=None):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_x_len = cell_x_len
        if cell_y_len:
            self._cell_y_len = cell_y_len
        else:
            self._cell_y_len = cell_x_len
        self._win = win
        self._cells = []
        self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self._num_cols):
            cell_col = []
            for row in range(self._num_rows):
                new_cell = Cell((self._cell_x_len * row + self._x), (self._cell_y_len * col + self._y), self._cell_x_len, self._cell_y_len, self._win)
                cell_col.append(new_cell)
            self._cells.append(cell_col)
        if self._win:
            for y in range(len(self._cells)):
                for x in range(len(self._cells[y])):
                    self._draw_cell(y, x)
    
    def _draw_cell(self, y, x):
        if self._win:
            self._cells[y][x].draw()
            self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top = False
        self._cells[-1][-1].has_bottom = False
        if self._win:
            self._draw_cell(0, 0)
            self._draw_cell(-1, -1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            if j-1 >= 0:
                if not self._cells[i][j-1].visited:
                    to_visit.append(self._cells[i][j-1])
            if j+1 < self._num_rows:
                if not self._cells[i][j+1].visited:
                    to_visit.append(self._cells[i][j+1])
            if i-1 >= 0:
                if not self._cells[i-1][j].visited:
                    to_visit.append(self._cells[i-1][j])
            if i+1 < self._num_cols:
                if not self._cells[i+1][j].visited:
                    to_visit.append(self._cells[i+1][j])
            if not to_visit:
                self._draw_cell(i, j)
                break
            rand_cell = random.randint(0, len(to_visit)-1)
            next_cell = to_visit[rand_cell]
            if next_cell._x1 > current_cell._x1:
                current_cell.has_right = False
                next_cell.has_left = False
                self._draw_cell(i, j)
                self._break_walls_r(i, j+1)
            if next_cell._x1 < current_cell._x1:
                current_cell.has_left = False
                next_cell.has_right = False
                self._draw_cell(i, j)
                self._break_walls_r(i, j-1)
            if next_cell._y1 > current_cell._y1:
                current_cell.has_bottom = False
                next_cell.has_top = False
                self._draw_cell(i, j)
                self._break_walls_r(i+1, j)
            if next_cell._y1 < current_cell._y1:
                current_cell.has_top = False
                next_cell.has_bottom = False
                self._draw_cell(i, j)
                self._break_walls_r(i-1, j)

    def _reset_cells_visited(self):
        for y in range(len(self._cells)):
            for x in range(len(self._cells[y])):
                self._cells[y][x].visited = False

    def solve(self):
        solved = self._solve_r(0,0)
        if solved:
            return True
        else:
            return False

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        if i+1 < self._num_cols and not current_cell.has_bottom:
            next_cell = self._cells[i+1][j]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                solved = self._solve_r(i+1, j)
                if solved:
                    return True
                current_cell.draw_move(next_cell, undo=True)
        if j+1 < self._num_rows and not current_cell.has_right:
            next_cell = self._cells[i][j+1]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                solved = self._solve_r(i, j+1)
                if solved:
                    return True
                current_cell.draw_move(next_cell, undo=True)
        if j-1 >= 0 and not current_cell.has_left:
            next_cell = self._cells[i][j-1]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                solved = self._solve_r(i, j-1)
                if solved:
                    return True
                current_cell.draw_move(next_cell, undo=True)
        if i-1 >= 0 and not current_cell.has_top:
            next_cell = self._cells[i-1][j]
            if not next_cell.visited:
                current_cell.draw_move(next_cell)
                solved = self._solve_r(i-1, j)
                if solved:
                    return True
                current_cell.draw_move(next_cell, undo=True)
        return False
