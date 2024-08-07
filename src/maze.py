from graphics import Cell, Point

import random
import time

class Maze:
    def __init__(self, x1, y1, 
                num_rows, num_cols, 
                cell_size_x, cell_size_y, 
                win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self._cells = []
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        if seed is not None:
            random.seed(seed)

        self._create_cells()
    
    def _create_cells(self):
        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                col.append(Cell(self.win))
            
            self._cells.append(col)
        
        # i == index of column, j == index of cell.
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        
        top_left = Point(self.x1 + (i * self.cell_size_x), 
                         self.y1 + (j * self.cell_size_y))
        bot_right = Point((self.x1 + self.cell_size_x) + (i * self.cell_size_x),
                           self.y1 + self.cell_size_y + (j * self.cell_size_y))

        cell = self._cells[i][j]
        cell.draw(top_left, bot_right)

        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        
        self.win.redraw()
        time.sleep(0.035)

    def _break_entrance_and_exit(self):
        first_col = first_row = 0
        entrance = self._cells[first_col][first_row]
        entrance.has_top_wall = False
        self._draw_cell(0, 0)

        last_col = self.num_cols - 1
        last_row = self.num_rows - 1
        exit = self._cells[last_col][last_row]
        exit.has_bot_wall = False
        self._draw_cell(last_col, last_row)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            to_visit = []

            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))

            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
                
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))

            if to_visit == []:
                self._draw_cell(i, j)
                return
            
            direction = random.randrange(len(to_visit))
            next_index = to_visit[direction]

            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)

                self._cells[i - 1][j].has_right_wall = False
                self._draw_cell(i - 1, j)

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)

                self._cells[i + 1][j].has_left_wall = False
                self._draw_cell(i + 1, j)

            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)

                self._cells[i][j - 1].has_bot_wall = False
                self._draw_cell(i, j - 1)

            if next_index[1] == j + 1:
                self._cells[i][j].has_bot_wall = False
                self._draw_cell(i, j)

                self._cells[i][j + 1].has_top_wall = False
                self._draw_cell(i, j + 1)

            self._break_walls_r(next_index[0], next_index[1])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i ,j):
        self._animate()
        self._cells[i][j].visited = True

        directions = []

        if self._cells[i][j] == self._cells[self.num_cols - 1][self.num_rows - 1]:
            return True

        if i > 0 and not self._cells[i - 1][j].visited:
            directions.append((i - 1, j))

        if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
            directions.append((i + 1, j)) # Dodał w prawo

        if j > 0 and not self._cells[i][j - 1].visited:
            directions.append((i, j - 1)) # Dodał w górę

        if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
            directions.append((i, j + 1)) # Dodał w lewo.

        for direction in directions:
            if direction[0] == i + 1:
                if not self._cells[i + 1][j].has_left_wall and not self._cells[i + 1][j].visited:
                    self._cells[i][j].draw_move(self._cells[i + 1][j])
                    if self._solve_r(i + 1, j) == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i + 1][j], undo = True)
            
            if direction[0] == i - 1:
                if not self._cells[i - 1][j].has_right_wall and not self._cells[i - 1][j].visited:
                    self._cells[i][j].draw_move(self._cells[i - 1][j])
                    if self._solve_r(i - 1, j) == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i - 1][j], undo = True)

            if direction[1] == j + 1:
                if not self._cells[i][j + 1].has_top_wall and not self._cells[i][j + 1].visited:
                    self._cells[i][j].draw_move(self._cells[i][j + 1])
                    if self._solve_r(i, j + 1) == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j + 1], undo = True)

            if direction[1] == j - 1:
                if not self._cells[i][j - 1].has_bot_wall and not self._cells[i][j - 1].visited:
                    self._cells[i][j].draw_move(self._cells[i][j - 1])
                    if self._solve_r(i, j - 1) == True:
                        return True
                    else:
                        self._cells[i][j].draw_move(self._cells[i][j - 1], undo = True)

        return False