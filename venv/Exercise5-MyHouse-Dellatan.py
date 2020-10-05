from graphics import *

# Creates the window
win = GraphWin("Exercise5-MyHouse-Dellatan", 400, 400)

# Draws the rectangular body of the house
rect = Rectangle(Point(150,200), Point(225, 130))
rect.draw(win)

# Draws the lines in-order to form a roof of the house
line1 = Line(Point(150, 130), Point(190,95))
line1.draw(win)
line2 = Line(Point(225,130), Point(190,95))
line2.draw(win)

# Draws the lines in-order to form a door of the house
line3 = Line(Point(180,200), Point(180, 165))
line3.draw(win)
line4 = Line(Point(200,200), Point(200,165))
line4.draw(win)
line5 = Line(Point(180,165), Point(200,165))
line5.draw(win)


# Waits for the user to close the window
win.getMouse()
win.wait()