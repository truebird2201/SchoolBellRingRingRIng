from tkinter import *
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

        Cell.Check()
    
    def __CheckVertical():
        for r in range(0, _MAXROW):
            for c in range(0, _MAXCOL - 3):
                if cells[r*_MAXROW + c].color == cells[r*_MAXROW + c + 1].color and \
                    cells[r*_MAXROW + c].color == cells[r*_MAXROW + c + 2].color and \
                    cells[r*_MAXROW + c].color == cells[r*_MAXROW + c + 3].color and \
                    cells[r*_MAXROW + c].color != "white":
                    return True
        return False

    def __CheckHorizontal():
        for r in range(0, _MAXROW-3):
            for c in range(0, _MAXCOL):
                if cells[r*_MAXROW + c].color == cells[(r+1)*_MAXROW + c].color and \
                    cells[r*_MAXROW + c].color == cells[(r+2)*_MAXROW + c].color and \
                    cells[r*_MAXROW + c].color == cells[(r+3)*_MAXROW + c].color and \
                    cells[r*_MAXROW + c].color != "white":
                    return True
        return False

    def __CheckDiag1():
        
        return False

    def __CheckDiag2():
        return False

    def Check():
        if (Cell.__CheckVertical() or Cell.__CheckHorizontal() or Cell.__CheckDiag1() or Cell.__CheckDiag2()):
            print(True)
            return True
        print(False)
        return False






window = Tk() # Create a window
window.title("Connect Four") # Set title

frame1 = Frame(window)
frame1.pack()
frame2 = Frame(window)
frame2.pack()
botton = Button(frame2,text="새로 시작",width=10,height=2).grid(row=0,column=0)
        
cells = [Cell(frame1, i//_MAXCOL, i%_MAXCOL, width = 20, height = 20) for i in range(_MAXROW*_MAXCOL)]

for cell in cells:
    cell.grid(row = cell.row, column = cell.col)

window.mainloop() # Create an event loop