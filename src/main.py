from graphics import Window
from maze import Maze

def main():
    
    win = Window(1024, 768)
    
    maze = Maze(50, 50, 3, 3, 50, 50, win)

    maze._break_entrance_and_exit()

    win.wait_for_close()
    
if __name__ == "__main__":
    main()