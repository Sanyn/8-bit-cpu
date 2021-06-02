from graphics import *
from ram import *
import math

class GPU:
    def __init__(self,s):
        self.ram = RAM(s,"noin")
        self.win = GraphWin("Visual",512,256)
        self.ram.clr()
    def clr(self):
        self.ram.clr()
    def get(self,addr):
        return self.ram.get(addr)
    def set(self,addr, val):
        self.ram.set(addr,val)
    def update(self):
        rect = Rectangle(Point(0,0), Point(512,256))
        rect.setOutline("white")
        rect.setFill("white")
        rect.draw(self.win)
        for i in range(self.ram.size):
            c=self.ram.get(i)
            for j in range(8):
                if(c%2 == 1):
                    x=(8*i)%64+j
                    y=math.floor(i/8)
                    rect=Rectangle(Point(x*8,y*8),Point(x*8+7,y*8+7))
                    rect.setOutline("black")
                    rect.setFill("black")
                    rect.draw(self.win)
                c >>= 1