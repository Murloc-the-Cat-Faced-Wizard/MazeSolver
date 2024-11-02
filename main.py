from Window import Window
from Point import Point
from Line import Line
from Cell import Cell


def main():
    win = Window(800, 600)
    cells = []
    for i in range(10):
        cell = Cell((45*i+15),15,40,win)
        cells.append(cell)
    for cell in cells:
        cell.draw()
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