from dice import *
from collections import Counter

class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        stackscore = 0
        if row >= 0 and row <= 5: # Ones ~ Sixes
            for dice in dices:
                if dice.getRoll() == (row + 1):
                    stackscore = stackscore + (row + 1)
        elif row >= 8 and row <= 12: # 3 of a kind
            templist = [0 for _ in range(6)]
            for dice in dices:
                if dice.getRoll() > 0 and dice.getRoll() < 7:
                    templist[dice.getRoll() - 1] += 1

            if row == 8: # 3 of a kind
                list_Max = max(templist)
                for i in range(6):
                    if list_Max > 2 and templist[i] >= list_Max:
                        stackscore = (i+1) * 3
            elif row == 9: # 4 of a kind
                list_Max = max(templist)
                for i in range(6):
                    if list_Max > 3 and templist[i] >= list_Max:
                        stackscore = (i+1) * 4
            elif row == 10: # Full House(25)
                if 3 in templist and 2 in templist:
                    stackscore = 25
            elif row == 11: # Samll Straight(30)
                for i in range(3):
                    if templist[i] >= 1 and \
                        templist[i + 1] >= 1 and \
                        templist[i + 2] >= 1 and \
                        templist[i + 3] >= 1:
                        stackscore = 30
            elif row == 12: # Large Straight(40)
                for i in range(2):
                    if templist[i] == 1 and \
                        templist[i] == templist[i + 1] and \
                        templist[i] == templist[i + 2] and \
                        templist[i] == templist[i + 3] and \
                        templist[i] == templist[i + 4]:
                        stackscore = 40
            
        elif row == 13: # Yahtzee(50)
            if dices[0].getRoll() == dices[1].getRoll() and \
                dices[0].getRoll() == dices[2].getRoll() and \
                dices[0].getRoll() == dices[3].getRoll() and \
                dices[0].getRoll() == dices[4].getRoll():
                stackscore = 50
        elif row == 14: # Chance
            for dice in dices:
                stackscore = stackscore + dice.getRoll()
            

        return stackscore

