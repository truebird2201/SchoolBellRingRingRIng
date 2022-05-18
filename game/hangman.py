import math
from tkinter import * # Import tkinter
from random import randint
    
class Hangman:

    def __init__(self):
        self.nMissChar = 7
        self.nCorrectChar=0
        self.hiddenWord = ''
        self.guessWord = []
        self.nMissedLetters=[]
        self.finished = 0
        global words
        self.hiddenWord = words[randint(0,len(words)-1)]
        for i in self.hiddenWord:
            self.guessWord.append('*')
        self.draw()

    def clear(self):
        
        self.nMissChar = 7
        self.nCorrectChar=0
        self.hiddenWord = ''
        self.guessWord = []
        self.nMissedLetters=[]
        self.finished = 0

        global words
        self.hiddenWord = words[randint(0,len(words)-1)]
        for i in self.hiddenWord:
            self.guessWord.append('*')
        self.draw()

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        radius = 20 # 반지름
        if self.nMissChar < 7:
            canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        if self.nMissChar < 6:
            canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger
            
        if self.nMissChar < 5:
            lx1 = 160 - radius * math.cos(math.radians(45))
            ly1 = 60 + radius * math.sin(math.radians(45))
            lx2 = 160 - (radius+60) * math.cos(math.radians(45))
            ly2 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(lx1, ly1, lx2, ly2, tags = "hangman")
        
        if self.nMissChar < 4:
            rx1 = 160 + radius * math.cos(math.radians(45))
            ry1 = 60 + radius * math.sin(math.radians(45))
            rx2 = 160 + (radius+60) * math.cos(math.radians(45))
            ry2 = 60 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(rx1, ry1, rx2, ry2, tags = "hangman")

        if self.nMissChar < 3:
            bx1 = 160
            by1 = 60 + radius
            bx2 = 160
            by2 = 60 + (radius+60)
            canvas.create_line(bx1, by1, bx2, by2, tags = "hangman")

        if self.nMissChar < 2:
            llx1 = 160
            lly1 = 60 + (radius+60)
            llx2 = 160 - (radius+60) * math.cos(math.radians(45))
            lly2 = lly1 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(llx1, lly1, llx2, lly2, tags = "hangman")

        if self.nMissChar < 1:
            rlx1 = 160
            rly1 = 60 + (radius+60)
            rlx2 = 160 + (radius+60) * math.cos(math.radians(45))
            rly2 = rly1 + (radius+60) * math.sin(math.radians(45))

            canvas.create_line(rlx1, rly1, rlx2, rly2, tags = "hangman")
        
        if self.finished == 2:
            canvas.create_line(153, 60, 158, 50, tags = "hangman")
            canvas.create_line(152, 50, 158, 60, tags = "hangman")
            canvas.create_line(168, 60, 173, 50, tags = "hangman")
            canvas.create_line(167, 50, 178, 60, tags = "hangman")
            canvas.create_oval(155, 65, 170, 75, tags = "hangman") # Draw the hanger

        

        word = ''
        word2 = ''
        for i in self.guessWord:
            word += i
        for i in self.nMissedLetters:
            word2 += i

        if self.finished == 0:
    
            canvas.create_text(250,200, text = "단어 추측 : {0}".format(word), font=("나눔고딕",10), fill = "Black", tags = "hangman")
            canvas.create_text(250,220, text = "틀린 단어 : {0}".format(word2), font=("나눔고딕",10), fill = "Black", tags = "hangman")
        if self.finished == 1:
            canvas.create_text(250,200, text = "{0} 맞았습니다 ".format(self.hiddenWord), font=("나눔고딕",10), fill = "Black", tags = "hangman")
            canvas.create_text(250,220, text = "게임을 계속 하려면 ENTER를 누르세요", font=("나눔고딕",10), fill = "Black", tags = "hangman")
        if self.finished == 2:
            canvas.create_text(250,200, text = "{0} 틀렸습니다 ㅠㅠ ".format(self.hiddenWord), font=("나눔고딕",10), fill = "Black", tags = "hangman")
            canvas.create_text(250,220, text = "게임을 계속 하려면 ENTER를 누르세요", font=("나눔고딕",10), fill = "Black", tags = "hangman")
            
        
        
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()
    
window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman
    
    if event.char >= 'a' and event.char <= 'z' and (event.char not in hangman.guessWord) and (event.char not in hangman.nMissedLetters) :
        if event.char in hangman.hiddenWord:
            for i in range (len(hangman.guessWord)):
                if event.char == hangman.hiddenWord[i]:
                    hangman.guessWord[i] = event.char
                    hangman.nCorrectChar += 1
                    if hangman.nCorrectChar == len(hangman.hiddenWord):
                        hangman.finished = 1

        else:
            hangman.nMissChar -= 1
            hangman.nMissedLetters.append(event.char)
            if hangman.nMissChar == 0:
                hangman.finished = 2
            
    elif event.keycode == 13 and hangman.finished != 0:
        hangman.clear()
    hangman.draw()
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = 'White', width = width, height = height)
canvas.pack()

hangman = Hangman()

# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop
