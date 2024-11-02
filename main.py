from Window import Window
from Point import Point
from Line import Line
from Cell import Cell
from Maze import Maze


def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)
    length = 40
    num_rows = win_width//length
    num_cols = win_height//length
    maze = Maze(1,1,num_rows,num_cols,length,win)
    win.wait_for_close()

main()
