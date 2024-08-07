from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(self.__root, bg='white', height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__is_running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True
        
        while self.__is_running == True:
            self.redraw()
    
    def close(self):
        self.__is_running = False
    
    def draw_line(self, line, fill_color='black'):
        line.draw(self.__canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bot_wall = True
        
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None

        self._win = win
        self.visited = False

    def draw(self, top_left, bot_right):
        self._x1 = top_left.x
        self._y1 = top_left.y
        self._x2 = bot_right.x
        self._y2 = bot_right.y
        
        left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        right_wall = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        bot_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))

        if self.has_left_wall:   
            self._win.draw_line(left_wall)
        else:
            self._win.draw_line(left_wall, fill_color='white')
        
        if self.has_right_wall:
            self._win.draw_line(right_wall)
        else:
            self._win.draw_line(right_wall, fill_color='white')

        if self.has_top_wall:
            self._win.draw_line(top_wall)
        else:
            self._win.draw_line(top_wall, fill_color='white')

        if self.has_bot_wall:
            self._win.draw_line(bot_wall)
        else:
            self._win.draw_line(bot_wall, fill_color='white')
    
    def draw_move(self, to_cell, undo=False):
        x_center = (self._x1 + self._x2)/2
        y_center = (self._y1 + self._y2)/2
        self._center = Point(x_center, y_center)

        x_center2 = (to_cell._x1 + to_cell._x2)/2
        y_center2 = (to_cell._y1 + to_cell._y2)/2
        to_cell._center = Point(x_center2, y_center2)
        
        move_line = Line(self._center, to_cell._center)

        if undo == False:
            fill_color = 'red'
        else:
            fill_color = 'gray'
        
        self._win.draw_line(move_line, fill_color=fill_color)