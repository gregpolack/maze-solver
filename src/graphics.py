from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        
        self.__root = Tk()
        self.__root.title("Maze Solver")

        self.__canvas = Canvas(self.__root, bg='white', height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.is_running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.is_running = True
        
        while self.__is_running == True:
            self.redraw()
    
    def close(self):
        self.is_running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
