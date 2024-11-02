import time
from Cell import Cell

class Maze:
    def __init__(self, x, y, num_rows, num_cols, cell_x_len, cell_y_len=None, win=None):
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

        self._create_cells()
        self._break_entrance_and_exit()

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
