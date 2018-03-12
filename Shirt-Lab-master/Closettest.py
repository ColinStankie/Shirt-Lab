"This is a test file with nothing here."
from MainCloset import *
from Graphics import *
def main():
    """makes a window for the program"""

    win.getMouse()
    win.close()

win = GraphWin("Clothes", 1000, 650)
win.setBackground("white")
main()