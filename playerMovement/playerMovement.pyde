def setup():
    size(500, 500, P3D)   
    global x
    global y
    global i
    stroke(255)
    noFill()
    x = width / 2
    y = height / 2
    frameRate(5)

def draw():
     background(100)         
     strokeWeight(10)
     strokeCap(SQUARE)
     chest()

def moveRight(rep):
    for i in range(0, rep * 5, 1):
        global x
        point(x + i, y)
    x = x + (5 * rep)
def moveLeft(rep):
    for i in range(0, rep * 5, 1):
        global x
        point(x - i, y)
        
        
    x = x - (5 * rep)

def moveUp(rep):
    for i in range(0, rep * 5, 1):
        global y
        point(x, y - i)

    y = y - (5 * rep)
def moveDown(rep):
    for i in range(0, rep * 5, 1):
        global y
        point(x, y + i)
    y = y + (5 * rep)

def keyPressed():
    if key == CODED:
        if keyCode == RIGHT:
            moveRight(1)
        elif keyCode == DOWN:
            moveDown(1)
        elif keyCode == UP:
            moveUp(1)
        elif keyCode == LEFT:
            moveLeft(1)
def chest(x,y):
    move = false
    if move:
    fill(255)
    rect(random(1,500),random(1,500),10,10)
    