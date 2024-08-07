from graphics import Window
from maze import Maze

def main():
    
    num_rows = 9
    num_cols = 9

    win = Window(1024, 768)
    
    maze = Maze(80, 80, num_rows, num_cols, 60, 60, win)

    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)
    maze._reset_cells_visited()
    maze.solve()

    win.wait_for_close()
    
if __name__ == "__main__":
    main()