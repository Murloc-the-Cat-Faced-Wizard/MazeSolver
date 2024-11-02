from Window import Window
from Point import Point
from Line import Line
from Cell import Cell


def main():
    win_width = 800
    win_height = 600
    win = Window(win_width, win_height)
    cells = []
    length = 40
    x_start = 1
    y_start = 1
    for col in range(win_height//length):
        for row in range(win_width//length):
            cell = Cell((length*row+x_start),(length*col+y_start),length,win)
            cells.append(cell)
    for cell in cells:
        cell.draw()
    cells[0].draw_move(cells[20])
    cells[1].draw_move(cells[2], True)
    #point1 = Point(400, 10)
    #point2 = Point(200, 590)
    #point3 = Point(690, 200)
    #point4 = Point(110, 200)
    #point5 = Point(600, 590)
    #win.draw_line(Line(point1, point2), "BLACK")
    #win.draw_line(Line(point2, point3), "RED")
    #win.draw_line(Line(point3, point4), "BLUE")
    #win.draw_line(Line(point4, point5), "GREEN")
    #win.draw_line(Line(point5, point1), "YELLOW")
    win.wait_for_close()

main()