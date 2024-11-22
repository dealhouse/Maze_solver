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

    def draw(self):
        if self._window is None:
            return
        if self.has_left_wall:
            self._window.draw_line(Line(Point(self.x1, self.y1), Point(self.x1, self.y2)), "black")
        if self.has_right_wall:
            self._window.draw_line(Line(Point(self.x2, self.y1), Point(self.x2, self.y2)), "black")
        if self.has_top_wall:
            self._window.draw_line(Line(Point(self.x1, self.y1), Point(self.x2, self.y1)), "black")
        if self.has_bottom_wall:
            self._window.draw_line(Line(Point(self.x1, self.y2), Point(self.x2, self.y2)), "black")

    def draw_move(self, to_cell, undo=False):
        center_coordinate = Point((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2)
        to_center_coordinate = Point((to_cell.x1 + to_cell.x2) / 2, (to_cell.y1 + to_cell.y2) / 2)
        if notundo:
            self._window.draw_line(Line(center_coordinate, to_center_coordinate), "red")
        else:
            self._window.draw_line(Line(center_coordinate, to_center_coordinate), "gray")

