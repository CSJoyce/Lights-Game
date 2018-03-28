import math

def setup(): 
    size(500, 500, P3D)
    noStroke()

def draw(): 
    background(0)
    lights()
    e1.display()
    translate(mouseX, mouseY)
    fill(255)
    sphere(30)
    e1.move(mouseX, mouseY)

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