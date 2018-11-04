from inputDialog import InputDialog
from graphics import *
from shotTracker import ShotTracker

def main():
    #create animation window
    win = GraphWin("Animation",640, 480, autoflush = False)
    win.setCoords(-10, -10, 210, 155)
    Line(Point(-10,0),Point(210,0)).draw(win)
    for x in range(0, 210, 50):
        Text(Point(x,-5),str(x)).draw(win)
        Line(Point(x,0),Point(x,2)).draw(win)

    #loop,each time through fires a single shot
    angle, vel, height = 45.0, 40.0, 2.0
    while True:
        # interact with the user
        inputwin = InputDialog(angle, vel, height)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Quit": # exit
            break

        #creat a shot and track until it hits ground or leaves window
        angle,vel,height = inputwin.getValues()
        shot = ShotTracker(win, angle, vel, height)
        while 0 <= shot.getY() <= 155  and -10 < shot.getX() <= 210:
            shot.update(1/50)
            update(50)
        #draw maximum Y position  of the ball when it begin to drop or leave the windows
        shot.drawMaxYball(win)

    win.close()


main()
