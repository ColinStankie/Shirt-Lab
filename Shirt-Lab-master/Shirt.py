from Graphics import *

class Shirt(object):
    """This creates a basic colored shirt"""
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color

    def drawShirt(self, x, y, color, win):
        shirt = Polygon(Point(x,y),Point(self.x + 125, self.y),Point(self.x + 125, self.y + 150),Point(self.x + 125, self.y + 125),Point(self.x + 175, self.y + 125),Point(self.x + 175, self.y + 175),Point(self.x + 150,self.y + 200),Point(self.x + 100, self.y + 200),Point(self.x + 75,self.y + 175))
        shirt.setFill(color)
        shirt.draw(win)



