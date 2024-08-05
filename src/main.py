from graphics import *

def main():
    win = Window(1024, 768)
    
    c1 = Cell(win)
    c1.draw(Point(50, 50), Point(70, 30))

    c2 = Cell(win)
    c2.draw(Point(100, 100), Point(130, 70))

    c1.draw_move(c2)

    win.wait_for_close()

if __name__ == "__main__":
    main()