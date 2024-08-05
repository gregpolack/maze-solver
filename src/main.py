from graphics import *

def main():
    win = Window(1024, 768)

    cell = Cell(win, Point(50, 50), Point(70, 30))
    cell.draw()

    cell = Cell(win, Point(100, 100), Point(130, 70))
    cell.draw()

    win.wait_for_close()

if __name__ == "__main__":
    main()