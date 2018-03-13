"This is a test file with nothing here."
from Shirt import *
from Graphics import *
def main():
    """makes a window for the program"""
    shirt = Shirt(100, 300, "blue", win)
    shirt1 = Shirt(125, 300, "purple", win)
    shir = Shirt(150, 300, "pink", win)
    shirt2 = Shirt(175, 300, "red", win)
    dfaf = Shirt(100, 300, "orange", win)
    long2 = Shirt(125, 300, "yellow", win)
    shirt3 = Shirt(150, 300, "green", win)
    shirt4 = Shirt(175, 300, "white", win)
    win.getMouse()
    win.close()

win = GraphWin("Clothes", 1000, 650)
win.setBackground(color_rgb(187,182,214))
main()