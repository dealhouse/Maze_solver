from window import Window
from line import Line
from point import Point

win = Window(800, 600)

line = Line(Point(100, 100), Point(300, 300))
line2 = Line(Point(300, 100), Point(100, 300))
win.draw_line(line, "red")
win.draw_line(line2, "blue")
win.wait_for_close()



