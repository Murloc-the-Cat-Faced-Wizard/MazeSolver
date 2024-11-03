from Point import Point
from Line import Line

class Cell:
    def __init__(self, x, y, length_x, length_y=None, win=None, left=True, right=True, top=True, bottom=True):
        self.has_left = left
        self.has_right = right
        self.has_top = top
        self.has_bottom = bottom
        self._length_x = length_x
        if length_y:
            self._length_y = length_y
        else:
            self._length_y = length_x
        self._x1 = x
        self._y1 = y
        self._x2 = x + length_x
        self._y2 = y + length_y
        self._win = win
        self.visited = False

    def draw(self):
        tl = Point(self._x1, self._y1)
        tr = Point(self._x2, self._y1)
        bl = Point(self._x1, self._y2)
        br = Point(self._x2, self._y2)
        if self.has_left:
            self._win.draw_line(Line(tl, bl), "GREEN")
        else:
            self._win.draw_line(Line(tl, bl), "#d9d9d9")
        
        if self.has_right:
            self._win.draw_line(Line(tr, br), "PURPLE")
        else:
            self._win.draw_line(Line(tr, br), "#d9d9d9")
        
        if self.has_top:
            self._win.draw_line(Line(tl, tr), "BLACK")
        else:
            self._win.draw_line(Line(tl, tr), "#d9d9d9")
        
        if self.has_bottom:
            self._win.draw_line(Line(bl, br), "BLUE")
        else:
            self._win.draw_line(Line(bl, br), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        self_center = Point(self._x1 + self._length_x//2, self._y1 + self._length_y//2)
        to_cell_center = Point(to_cell._x1 + to_cell._length_x//2, to_cell._y1 + to_cell._length_y//2)
        if undo:
            self._win.draw_line(Line(self_center, to_cell_center), "GRAY")
        else:
            self._win.draw_line(Line(self_center, to_cell_center), "RED")
        
