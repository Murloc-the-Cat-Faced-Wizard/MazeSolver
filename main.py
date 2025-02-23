from Window import Window
from Point import Point
from Line import Line
from Cell import Cell
from Maze import Maze


def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)
    cells_per_row = 12
    cells_per_col = 10
    x_offset = 20
    y_offset = 20
    length_x = (win_width-2*x_offset)//cells_per_row
    length_y = (win_height-2*y_offset)//cells_per_col
    maze = Maze(x_offset, y_offset, cells_per_row, cells_per_col, length_x, length_y, win, None)
    maze.solve()
    win.wait_for_close()

main()
