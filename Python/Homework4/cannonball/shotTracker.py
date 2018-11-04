# shotTracker.py

from projectile import Projectile
from graphics import *


class ShotTracker:

    """This is is a graphical object that acts like a cannonball."""

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot . angle, velocity,
        and height are initial proj ectile parameters """
        self.proj = Projectile(angle, velocity, height)
        self.marker =Circle(Point(0, height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

        # maxball
        self.maxball = Circle(Point(0, height), 3)
        

    def update(self, dt):
        """Move the shot dt seconds farther along its flight"""
        # update the proj ectile
        self.proj.update(dt)
        # move the circle to the new proj ectile location
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)


    def getX(self):
        """return the current x coordinate of the shot's center"""
        return self.proj.getX()


    def getY(self):
        """    11 11 11
        return the current y coordinate of the shot's center"""
        return self.proj.getY()
    
    def drawMaxYball(self,win):
        dx,dy = self.proj.getMaxY()
        self.maxball = Circle(Point(dx,dy), 3)
        self.maxball.setFill("green")
        self.maxball.setOutline("green")


        self.maxball.draw(win)
         

    def undraw(self):
        """undraw the shot"""
        self.marker.undraw()



