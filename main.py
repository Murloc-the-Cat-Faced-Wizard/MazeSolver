from Window import Window
from Point import Point
from Line import Line


def main():
    win = Window(800, 600)
    point1 = Point(450, 450)
    point2 = Point(50, 50)
    line1 = Line(point1, point2)
    win.draw_line(line1, "BLACK")
    win.draw_line(Line(Point(700,2), Point(5,500)), "RED")
    win.draw_line(Line(Point(400,2), Point(400,598)), "BLUE")
    win.wait_for_close()

main()