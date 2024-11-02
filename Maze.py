import time
from Cell import Cell

class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_len, win):
        self._x = x
        self._y = y
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_len = cell_len
        self._win = win
        self._cells = []

        self._create_cells()

    def _create_cells(self):
        for row in range(self._num_rows):
            cell_row = []
            for col in range(self._num_cols):
                new_cell = Cell((self._cell_len * row + self._x), (self._cell_len * col + self._y), self._cell_len, self._win)
                cell_row.append(new_cell)
            self._cells.append(cell_row)
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        self._cells[i][j].draw()
        self._animate()
    
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
