from line import Line
from point import Point
from window import Window
class Cell:
    def __init__(self, x1, x2, y1, y2, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, _window):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._window = _window

    def draw(self, x1, x2, y1, y2):
        if self.has_left_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x1, y2)), "black")
        if self.has_right_wall:
            self._window.draw_line(Line(Point(x2, y1), Point(x2, y2)), "black")
        if self.has_top_wall:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y1)), "black")
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(x1, y2), Point(x2, y2)), "black")
