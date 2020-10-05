from graphics import *

# Creates the window
win = GraphWin("Exercise5-Olympics-Dellatan", 350, 350)

# Draws the blue ring aligned with its x & y axis, sets the blue color and the width of the ring
blueRing = Oval(Point(100, 150), Point(150, 100))
blueRing.setOutline(color_rgb(35,112,185))
blueRing.setWidth(3.5)
blueRing.draw(win)

# Draws the black ring aligned with its x & y axis, sets the black color and the width of the ring
blackRing = Oval(Point(150, 150),Point(200, 100))
blackRing.setOutline(color_rgb(15,15,15))
blackRing.setWidth(3.5)
blackRing.draw(win)

# Draws the red ring aligned with its x & y axis, sets the red color and the width of the ring
redRing = Oval(Point(200,150), Point(250,100))
redRing.setOutline(color_rgb(218,83,48))
redRing.setWidth(3.5)
redRing.draw(win)

# Draws the yellow ring aligned with its x & y axis, sets the yellow color and the width of the ring
yellowRing = Oval(Point(125, 175), Point(175, 125))
yellowRing.setOutline(color_rgb(253,224,106))
yellowRing.setWidth(3.5)
yellowRing.draw(win)

# Draws the green ring aligned with its x & y axis, sets the green color and the width of the ring
greenRing = Oval(Point(175,175), Point(225,125))
greenRing.setOutline(color_rgb(112,191,84))
greenRing.setWidth(3.5)
greenRing.draw(win)


# Waits for the user to close the window
win.getMouse()
win.wait()