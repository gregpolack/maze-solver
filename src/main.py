from graphics import Window, Line, Point

def main():
    win = Window(1024, 768)

    line_one = Line(Point(50, 50), Point(90, 110))
    win.draw_line(line_one, "black")
    
    line_two = Line(Point(100, 120), Point(150, 180))
    win.draw_line(line_two, "red")

    win.wait_for_close()

if __name__ == "__main__":
    main()