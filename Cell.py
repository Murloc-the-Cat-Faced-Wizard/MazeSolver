from Point import Point
from Line import Line

class Cell:
    def __init__(self, x, y, length, win, left=True, right=True, top=True, bottom=True):
        self.has_left = left
        self.has_right = right
        self.has_top = top
        self.has_bottom = bottom
        self._x1 = x
        self._y1 = y
        self._x2 = x + length
        self._y2 = y + length
        self._win = win

    def draw(self):
        tl = Point(self._x1, self._y1)
        tr = Point(self._x2, self._y1)
        bl = Point(self._x1, self._y2)
        br = Point(self._x2, self._y2)
        if self.has_left:
            self._win.draw_line(Line(tl, bl), "GREEN")
        if self.has_right:
            self._win.draw_line(Line(tr, br), "RED")
        if self.has_top:
            self._win.draw_line(Line(tl, tr), "BLACK")
        if self.has_bottom:
            self._win.draw_line(Line(bl, br), "BLUE")
        
