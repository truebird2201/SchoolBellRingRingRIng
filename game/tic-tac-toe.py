from tkinter import *
from tkinter import font

class TicTacToe:
    window = Tk()
    img_empty = PhotoImage(file = "image/Title.gif").zoom(3)
    img_O = PhotoImage(file = "image/o.gif").zoom(3)
    img_X = PhotoImage(file = "image/x.gif").zoom(3)

    def __init__(self):
        self.window.geometry("300x450+450+450")
        
        self.turn = 'X'
        self.run = True

        self.fontTitle = font.Font(self.window, size=16, weight='bold', family = '윤고딕230')

        self.frameTitle = Frame(self.window, padx=10, pady=10, bg='#ffc4c4')                            # 제목 프레임
        self.frameTitle.pack(side="top",fill="both")

        self.MainText = Label(self.frameTitle, font = self.fontTitle, text="TIC - TAC - TOE GAME",bg='#fff8dd')           # 제목 적기
        self.MainText.pack(anchor="center", fill="both")

        self.frame = Frame(self.window, bg='#fff8dd')
        self.frame.pack(side="top",fill="both")

        self.frameResult = Frame(self.window, padx=10, pady=10, bg='#ffc4c4')                             # 하단 설명 프레임  
        self.frameResult.pack(side="bottom",fill="both")

        self.ResultText = Label(self.frameResult, font = self.fontTitle, text=self.turn + "의 차례",bg='#fff8dd')        # 하단 설명 적기
        self.ResultText.pack(anchor="center", fill="both")

        self.buttonList = []
        for r in range(3):
            for c in range(3):
                if r == 0:
                    self.buttonList.append(Button(self.frame,image=self.img_empty,text=0, command=lambda R=r, C=c:self.press(R,C),width=94,height=94,bg = '#ffd6d6' ))
                elif r == 1:
                    self.buttonList.append(Button(self.frame,image=self.img_empty,text=0, command=lambda R=r, C=c:self.press(R,C),width=94,height=94,bg = '#feffd6' ))
                elif r == 2:
                    self.buttonList.append(Button(self.frame,image=self.img_empty,text=0, command=lambda R=r, C=c:self.press(R,C),width=94,height=94,bg = '#d8ffd6' ))
                self.buttonList[r*3+c].grid(row=r,column=c)

    def press(self,r,c):
        if not self.run:
            return

        if self.buttonList[r*3+c]['text'] == 0:
            if self.turn == 'X':
                self.buttonList[r*3+c].configure(image=self.img_X, text=1)
                self.turn = 'O'
            elif self.turn == 'O':
                self.buttonList[r*3+c].configure(image=self.img_O, text=-1)
                self.turn = 'X'
            self.ResultText.configure(text=self.turn + "의 차례")

        self.Referee()
            

    def Referee(self):
        indexes = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        result = []
        for index in indexes:
            result.append(sum([self.buttonList[d]['text'] for d in index]))

        if 3 in result:
            self.turn = 'X'
            self.run = False
        if -3 in result:
            self.turn = 'O'
            self.run = False

        if not 0 in [b['text'] for b in self.buttonList]:
            self.run = False
            self.turn = ''

        if not self.run:
            if self.turn == 'O' or self.turn == 'X':
                self.ResultText.configure(text=self.turn + " 승리! 게임이 끝났습니다.")
            else:
                self.ResultText.configure(text="무승부! 게임이 끝났습니다.")
    
    def loop(self):
        self.window.mainloop()
    
ttt = TicTacToe()
ttt.loop()