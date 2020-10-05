from graphics import *

# Creates the window
win = GraphWin("Exercise5-MyName-Dellatan", 400, 400)

# Draws rectangle shape aligned with the x & y axis, and length and width size with blue fill
rect = Rectangle(Point(50, 100), Point(350, 300))
rect.setFill("blue")
rect.draw(win)

# Draws text aligned with the x & y axis with red fill
text = Text(Point(200,200), "John Kyle L. Dellatan")
text.setFill("Red")
text.draw(win)

# Waits for the user to close the window
win.getMouse()
win.wait()