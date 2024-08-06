from graphics import Cell, Point
import time

class Maze:
    def __init__(self, x1, y1, 
                num_rows, num_cols, 
                cell_size_x, cell_size_y, 
                win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._create_cells()
    
    def _create_cells(self):
        self._cells = []

        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                col.append(Cell(self.win))
            
            self._cells.append(col)
        
        # i == index of column, j == index of cell.
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        
        top_left = Point(self.x1 + (i * self.cell_size_x), 
                         self.y1 + (j * self.cell_size_y))
        bot_right = Point((self.x1 + self.cell_size_x) + (i * self.cell_size_x),
                           self.y1 + self.cell_size_y + (j * self.cell_size_y))

        cell = Cell(self.win)
        cell.draw(top_left, bot_right)

        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        
        self.win.redraw()
        time.sleep(0.05)
