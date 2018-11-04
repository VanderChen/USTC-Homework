#import math

from math import sin , cos, radians


class Projectile:

    def __init__(self, angle, vel, height):
        self.xpos = 0.0
        self.ypos = height
        self.maxxpos = 0.0
        self.maxypos = height
        self.maxflag = False
        theta = radians(angle)
        self.xvel = vel * cos(theta)
        self.yvel = vel * sin(theta)


    def getX(self):
        return self.xpos


    def getY(self):
        return self.ypos
    


    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8 # yvel>=0  decrease before the ball drop down
        avgyvel =  (self.yvel + yvel1)/2.0  # average yvel
        #judgeMaxY(avgvel,time)
        if avgyvel <= 0 and self.maxflag == False: # judge current  yvel , if it <= 0 ,the current ypos is the max ypos
            self.maxypos = self.ypos + time * avgyvel/2
            self.maxxpos = self.xpos
            self.maxflag = True
        elif self.maxflag == False and avgyvel > 0 and self.xpos >= 210: # ball leaves the window from right
            self.maxypos = self.ypos
            self.maxxpos = 210
        elif self.maxflag == False and avgyvel > 0 and self.ypos >= 152: # ball leaves the window from top
            self.maxypos = 155
            self.maxxpos = self.xpos


        self.ypos = self.ypos + time * avgyvel
        self.yvel = yvel1


    def getMaxY(self):
        return self.maxxpos,self.maxypos


