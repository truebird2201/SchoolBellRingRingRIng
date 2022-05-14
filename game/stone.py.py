from tkinter import *
from tkinter import font
from turtle import color
from setuptools import Command

_MAXROW = 6
_MAXCOL = 7
Turn="red"
cells=[]
restart_Text = "새로 시작"
process_button=None
fin = False

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

    def setbg(self, bg):
        self.configure(background=bg)

    def clicked(self,event): # red 또는 yellow 돌 놓기.
        if ((((self.row!=_MAXROW-1) and cells[(self.row+1)][self.col].color!="white") or self.row==_MAXROW-1) and self.color == "white") and fin==False:
            
            global Turn
            self.setColor(Turn)
            self.Check()
            Turn = "red" if self.color != "red" else "yellow"
            
    
    def __CheckVertical():
        global Turn
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL - 3):
                if cells[r][c].color == cells[r][c+1].color and \
                    cells[r][c].color == cells[r][c+2].color and \
                    cells[r][c].color == cells[r][c+3].color and \
                    cells[r][c].color != "white":
                    cells[r][c].setbg(Turn)
                    cells[r][c+1].setbg(Turn)
                    cells[r][c+2].setbg(Turn)
                    cells[r][c+3].setbg(Turn)
                    return True
        return False

    def __CheckHorizontal():
        for r in range(0, _MAXROW-3):
            for c in range(0, _MAXCOL):
                if cells[r][c].color == cells[r+1][c].color and \
                    cells[r][c].color == cells[r+2][c].color and \
                    cells[r][c].color == cells[r+3][c].color and \
                    cells[r][c].color != "white":
                    cells[r][c].setbg(Turn)
                    cells[r+1][c].setbg(Turn)
                    cells[r+2][c].setbg(Turn)
                    cells[r+3][c].setbg(Turn)
                    return True
        return False

    def __CheckDiag1():
        global Turn
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL):
                if r + 3 < _MAXROW and c + 3 < _MAXCOL and \
                    cells[r][c].color == cells[r+1][c+1].color and \
                    cells[r][c].color == cells[r+2][c+2].color and \
                    cells[r][c].color == cells[r+3][c+3].color and \
                    cells[r][c].color != "white":
                    cells[r][c].setbg(Turn)
                    cells[r+1][c+1].setbg(Turn)
                    cells[r+2][c+2].setbg(Turn)
                    cells[r+3][c+3].setbg(Turn)
                    return True
        return False

    def __CheckDiag2():
        global Turn
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL):
                if r + 3 < _MAXROW and c - 3 > 0 and \
                    cells[r][c].color == cells[r+1][c-1].color and \
                    cells[r][c].color == cells[r+2][c-2].color and \
                    cells[r][c].color == cells[r+3][c-3].color and \
                    cells[r][c].color != "white":
                    cells[r][c].setbg(Turn)
                    cells[r+1][c-1].setbg(Turn)
                    cells[r+2][c-2].setbg(Turn)
                    cells[r+3][c-3].setbg(Turn)
                    return True
        return False

    def Check(self):
        if (Cell.__CheckVertical() or Cell.__CheckHorizontal() or Cell.__CheckDiag1() or Cell.__CheckDiag2()):
            print(True)
            process_button.configure(text=Turn+"의 승리 ! ")
            global fin
            fin=True
            

def press():
    if (process_button['text'] == "새로 시작"):
        reset()
    else:
        process_button.configure(text="새로 시작")

def reset():
    global fin, Turn
    fin=False
    Turn = "red"
    for r in range(_MAXROW):
        for c in range(_MAXCOL):
            cells[r][c].setColor("white")
            cells[r][c].setbg("blue")

            
            
            
    


window = Tk() # Create a window
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()

gameframe = Frame(window)
gameframe.pack()

frameResult = Frame(gameframe,padx=12, pady=4, bg='#ffc4c4')                            # 결과 프레임
frameResult.pack(side="bottom",fill="both")

cells = [[Cell(frame1, r, c, width = 20, height = 20) for c in range(_MAXCOL)] for r in range(_MAXROW)]
fontTitle = font.Font(window, size=10, weight='bold', family = '윤고딕230')

process_button = Button(frameResult,command=press,width=20, font = fontTitle, text=restart_Text,bg='#fff8dd')
process_button.pack(anchor="center", fill="both")

for cell in cells:
    for c in cell:
        c.grid(row = c.row, column = c.col)

window.mainloop() # Create an event loop