"""
OOP 와 tkinter 를 이용한 MAZE 그리기
"""
import time
import sys
import tkinter as tk

UNIT = 40
MAZE_H = 6
MAZE_W = 6

class Maze:
    def __init__(self):

        self.build_maze()

    def build_maze(self):
        self.window = tk.Tk()  # main window create
        self.window.title("MAZE with Q-Learning")
        self.window.geometry('{}x{}'.format(MAZE_W*UNIT, MAZE_H*UNIT)) # window size
        # canvas create
        self.canvas = tk.Canvas(self.window, bg='white', width=MAZE_W*UNIT, height=MAZE_H*UNIT) 
        # horizontal line
        for c in range(0, MAZE_W*UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_W*UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        # vertical line
        for r in range(0, MAZE_H*UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H*UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)
        
        self.originX = 20
        self.originY = 20

        goal_centerX = self.originX + UNIT * 5 
        goal_centerY = self.originY + UNIT * 5

        self.goal = self.canvas.create_oval(
            goal_centerX - 15, goal_centerY - 15,
            goal_centerX + 15, goal_centerY + 15, fill='yellow'
        )

        self.draw_rect()

        self.canvas.pack()

    def draw_rect(self):
        self.rect = self.canvas.create_rectangle(
            self.originX - 15, self.originY - 15,
            self.originX + 15, self.originY + 15, fill='red'
        )

    def render(self):
        time.sleep(0.1)  # 0.1 초 정지
        self.window.update()

if __name__ == '__main__':
    maze = Maze()
    maze.window.mainloop()