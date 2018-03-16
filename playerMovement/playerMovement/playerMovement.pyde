
def setup():
    size(400, 400)
    background(100)
    global x
    global y
    x = width / 2
    y = height / 2
    frameRate(10)

def draw():
    fill(255)
    strokeWeight(1)

def moveRight(rep):
        for i in range(0, rep * 5, 1):
         global x
         point(x+i, y)
        x = x + (5 * rep)

def moveLeft(rep):
     for i in range(0, rep * 5, 1):
      global x
      point(x-i, y)
      x = x - (5 * rep)

def moveUp(rep):
     for i in range(0, rep * 5, 1):
         global y
         point(x, y - i)

     y = y - (5 * rep)
def moveDown( rep):
     for i in range(0, rep * 5, 1):
         global y
         point(x, y + i)

     y = y + (5 * rep)

def keyPressed():
     if key == CODED:
         if keyCode == RIGHT:
             moveRight(1)
         elif keyCode == LEFT:
             moveLeft(1)
         else:
             keyCode == UP
         moveUp(1)
     else:
         keyCode == DOWN
     moveDown(1)
