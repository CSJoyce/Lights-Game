import math
import random

def setup(): 
    size(500, 500, P3D)
    noStroke()

def draw(): 
    background(0)
    e1.display()
    e2.display()
    c1.hover()
    c1.display()
    translate(mouseX, mouseY)
    fill(255)
    sphere(20)
    e1.move(mouseX, mouseY)
    e2.move(mouseX, mouseY)
    c1.doCol(e1.x, e1.y)
    c1.doCol(e2.x, e1.y)
    c1.doCol(e1.x+20, e1.y)
    c1.doCol(e2.x+20, e1.y)

class Chest(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.trans = 0

    def display(self):
        fill(250, 217, 53, self.trans)
        rect(self.x-2, self.y-2, 64, 34)
        fill(52, 40, 11, self.trans)
        rect(self.x, self.y, 60, 30)
        fill(250, 217, 53, self.trans)
        rect(self.x+27, self.y+3, 4, 8)
        fill(0, self.trans)
        rect(self.x-2, self.y+12, 64, 2)
        
        if mouseX > self.x-2 and mouseX < self.x+62 and mouseY > self.y-12 and mouseY < self.y+32:
            fill(255)
            textSize(32)
            text("word", 20, 20)
    
    def doCol(self, x, y):
        dist = sqrt((x-mouseX)*(x-mouseX) + (y-mouseY)*(y-mouseY))
        if dist < 20 + 10:
            noLoop()
            fill(255, 0, 0)
            rect(-1000, -1000, 10000, 10000)
            fill(0)
            textSize(32)
            text("You Died", 20, 10)
            
    
    def hover(self):
        dist = sqrt((self.x-mouseX)*(self.x-mouseX)+(self.y-mouseY)*(self.y-mouseY))
        if dist < 60:
            self.trans = (60 - dist)*3
        else:
            self.trans = 0
        
        

class Enemy(object):
    def __init__(self, x, y, speed):
        self.x = x 
        self.y = y
        self.speed = speed
    
    def display(self):
        fill(255, 10, 10)
        ellipse(self.x, self.y, 10, 10)
        ellipse(self.x +20, self.y, 10, 10)
    
    def move(self, playerX, playerY): # chase movement
        # Movement along x direction
       # if self.x > playerX:
        #    self.x -= self.speed
        #elif self.x < playerX:
        #    self.x += self.speed
        # Movement along y direction
       # if self.y < playerY:
        #    self.y += self.speed
        #elif self.y > playerY:
        #    self.y -= self.speed
        ang = atan2((playerY - self.y), (playerX - self.x))
        self.x += self.speed*cos(ang)
        self.y += self.speed*sin(ang)

e1 = Enemy(250, 250, 5)
e2 = Enemy(300, 300, 10)
c1 = Chest(random.randrange(450), random.randrange(450))