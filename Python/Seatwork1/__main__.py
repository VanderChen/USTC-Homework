from pokerapp import *
from guipoker import *
from start import *

def main():
    start = Start()

    ans = start.clickOn()
    if ans == "Start":
        start.close()
        inter = GraphicsInterface()
        app = PokerApp(inter)
        app.run()
        start.close()

    elif ans == "Quit":
        start.close()

if __name__ == '__main__':
    main()


