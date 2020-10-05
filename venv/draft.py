from graphics import *

win = GraphWin("draft window", 350, 650)

rect = Rectangle(Point(10,30), Point(40,70))
rect.setFill("blue")
rect.draw(win)

text = Text(Point(100, 50), "hoh")
text.draw(win)

line = Line(Point(50, 100), Point(100, 50))
line.draw(win)

win.getMouse()
win.close()