"This is a test file with nothing here."
from Shirt import *
from Graphics import *
def main():
    """makes a window for the program"""
    shirt = Shirt(300, 300, "blue", win)
    shirt.drawShirt(300,300,"blue",win)
    win.getMouse()
    win.close()

win = GraphWin("Clothes", 1000, 650)
win.setBackground("white")
main()