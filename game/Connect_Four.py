from tkinter import *

from setuptools import Command
_MAXROW = 6
_MAXCOL = 7

class Cell(Canvas):
    global cells
    def __init__(self, parent, row, col, width = 20, height = 20):
        Canvas.__init__(self, parent, width = width, height = height, \
        bg = "blue", borderwidth = 2)
        self.color = "white"
        self.row = row
        self.col = col
        self.create_oval(4, 4, 20, 20, fill = "white", tags="oval")
        self.bind("<Button-1>", self.clicked)

    def setColor(self, color):
        self.delete("oval")
        self.color = color
        self.create_oval(4, 4, 20, 20, fill = self.color, tags="oval")

    def clicked(self,event): # red 또는 yellow 돌 놓기.
        nextcolor = "red" if self.color != "red" else "yellow"
        self.setColor(nextcolor)

        self.Check()
    
    def __CheckVertical():
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL - 3):
                if cells[r][c].color == cells[r][c+1].color and \
                    cells[r][c].color == cells[r][c+2].color and \
                    cells[r][c].color == cells[r][c+3].color and \
                    cells[r][c].color != "white":
                    return True
        return False

    def __CheckHorizontal():
        for r in range(0, _MAXROW-3):
            for c in range(0, _MAXCOL):
                if cells[r][c].color == cells[r+1][c].color and \
                    cells[r][c].color == cells[r+2][c].color and \
                    cells[r][c].color == cells[r+3][c].color and \
                    cells[r][c].color != "white":
                    return True
        return False

    def __CheckDiag1():
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL):
                if r + 3 < _MAXROW and c + 3 < _MAXCOL and \
                    cells[r][c].color == cells[r+1][c+1].color and \
                    cells[r][c].color == cells[r+2][c+2].color and \
                    cells[r][c].color == cells[r+3][c+3].color and \
                    cells[r][c].color != "white":
                    return True
        return False

    def __CheckDiag2():
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL):
                if r + 3 < _MAXROW and c - 3 > 0 and \
                    cells[r][c].color == cells[r+1][c-1].color and \
                    cells[r][c].color == cells[r+2][c-2].color and \
                    cells[r][c].color == cells[r+3][c-3].color and \
                    cells[r][c].color != "white":
                    return True
        return False

    def Check(self):
        if (Cell.__CheckVertical() or Cell.__CheckHorizontal() or Cell.__CheckDiag1() or Cell.__CheckDiag2()):
            print(True)
            


def reset(list):
    list = [[Cell(frame1, r, c, width = 20, height = 20) for c in range(_MAXCOL)] for r in range(_MAXROW)]



window = Tk() # Create a window
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
cells = [[Cell(frame1, r, c, width = 20, height = 20) for c in range(_MAXCOL)] for r in range(_MAXROW)]
botton = Button(frame2,text="새로 시작",width=10,height=2).grid(row=0,column=0, command=reset(cells))
        
for cell in cells:
    for c in cell:
        c.grid(row = c.row, column = c.col)

window.mainloop() # Create an event loop