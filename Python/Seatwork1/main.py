from pokerapp import *
from guipoker import *
from start import *

start = Start()


def run():
    ans = start.clickOn()
    if ans == "Start":
        start.close()
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()
        start.close()

    elif ans == "Quit":
        start.close()


run()


