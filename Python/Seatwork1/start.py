from graphics import *
from pokerapp import PokerApp
from button import Button
from cdieview import ColorDieView

class Start:

    def __init__(self):
        self.win = GraphWin("Dice Poker", 600, 400)
        self.win.setBackground("green3")
        banner = Text(Point(300, 30), "Python  Poker  Parlor")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300, 380), "Welcome to the Dice Table")
        self.msg.setSize(18)
        self.msg.draw(self.win)
        self.buttons = []


        b = Button(self.win, Point(300, 230), 400, 40, "Start")
        self.buttons.append(b)

        b = Button(self.win, Point(570, 375), 40, 30, "Quit")
        self.buttons.append(b)



    def clickOn(self):
        ans = self.choose(["Start", "Quit"])
        self.msg.setText("")
        return ans

    def close(self):
        self.win.close()

    def choose(self, choices):
        buttons = self.buttons

        # activate choice buttons, deactivate others
        for b in buttons:
            if b.getLabel() in choices:
                b.activate()
            else:
                b.deactivate()

        # get mouse clicks until an active button is clicked
        while True:
            p = self.win.getMouse()
            for b in buttons:
                if b.clicked(p):
                    return b.getLabel()  # function exit here.