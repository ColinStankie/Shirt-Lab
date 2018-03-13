from Graphics import *

class Shirt(object):
    """This creates a basic colored shirt"""
    def __init__(self, x, y, color, win):
        self.x = x
        self.y = y
        self.color = color
        self.drawShirt( x, y, color, win)

    def drawShirt(self, x, y, color, win):
        shirt = Polygon(Point(x,y),Point(self.x + 125, self.y),Point(self.x + 125, self.y - 150),Point(self.x + 125, self.y - 125),Point(self.x + 175, self.y - 125),Point(self.x + 175, self.y - 175),Point(self.x + 150,self.y - 200),Point(self.x + 100, self.y - 200),Point(self.x + 75,self.y - 175),Point(self.x + 50,self.y - 175),Point(self.x +25,self.y - 200),Point(self.x -25,self.y -200),Point(self.x -50,self.y -175),Point(self.x-50,self.y-125),Point(self.x,self.y-125),Point(self.x,self.y-150))
        shirt.setFill(color)
        shirt.draw(win)


class LongSleeve(Shirt):
    def __init__(self, x, y, color, win):
        super(LongSleeve, self).__init__(x, y, color, win)
        self.drawSleeve(x, y, color, win)
    def drawSleeve(self,x,y, color, win):
        super().drawShirt(x, y, color, win)
        sleeve1 = Rectangle(Point(x + 125, y - 125), Point(x + 175, y - 25))
        sleeve2 = Rectangle(Point(x - 50, y - 125), Point(x, y - 25))
        sleeve1.setFill(color)
        sleeve2.setFill(color)
        sleeve1.draw(win)
        sleeve2.draw(win)



