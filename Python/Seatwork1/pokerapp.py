# pokerapp.py

from dice import Dice
from tkinter import *
import tkinter.messagebox as messagebox

class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):

        while self.money >= 10:
            ans = self.interface.clickOn()
            if ans == "Roll Dice":
                self.playRound()
            elif ans == "Help":
                self.help()
            elif ans == "Rank":
                self.showRank()
            else:
                break
        self.writeRank()
        self.interface.close()


    def writeRank(self):
        with open('rank.txt', 'r') as f:
            rankmessage = f.read()
            rankList = rankmessage.split(",")
            if self.money > int(rankList[0]):
                rankList[0] = str(self.money)

                rankList = list(map(int, rankList))
                rankList.sort()
                rankList = list(map(str, rankList))

            s = ','.join(rankList)

        with open('rank.txt', 'w') as f:
            f.write(s)


    def showRank(self):
        with open('rank.txt', 'r') as f:
            s = f.read()
            # rankList = rankmessage.split(",").sort(reverse=True)
            # s = ""
            # for socre in rankList:
            #     s = s +socre +"\n"
        messagebox.showinfo("HELP MESSAGE", "%s" % s)

    def help(self):
        helpmessage = "1.玩家从 100 美元开始。\n" \
                      "2.每轮要花 10 美元。这个数额在一轮开始时从玩家的钱中扣除。" \
                      "3.玩家最初掷出完全随机的一手牌（即掷出所有五个骰子）。\n" \
                      "4.玩家有两次机会，通过重掷部分或全部骰子来增强这手牌。\n" \
                      "5.在这手牌结束时，玩家的钱根据如下所列支付策略更新\n" \
                      "两对\t|\t5美元\n" \
                      "三张同号\t|\t8美元\n" \
                      "满堂红\t|\t12美元\n" \
                      "四张同号\t|\t15美元\n" \
                      "顺子\t|\t20美元\n" \
                      "五张同号\t|\t30美元\n"
        messagebox.showinfo("HELP MESSAGE", "%s" % helpmessage)

    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

