from graphics import Window
from maze import Maze

def main():
    
    win = Window(1024, 768)
    
    maze = Maze(50, 50, 10, 10, 50, 50, win)

    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)

    win.wait_for_close()
    
if __name__ == "__main__":
    main()