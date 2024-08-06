from graphics import Window
from maze import Maze

def main():
    
    win = Window(1024, 768)
    
    Maze(50, 50, 13, 19, 50, 50, win)
    
    win.wait_for_close()
    
if __name__ == "__main__":
    main()