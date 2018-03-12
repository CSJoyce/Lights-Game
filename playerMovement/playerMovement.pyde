def setup():
    size(400,400)
    background(100)
    x = width/2
    y = height/2   
    frameRate(10)  
def draw():
    fill(255)
    strokeWeight(2)
    
def moveleft(int):
    for i in range(0, rep*5, 1):
        point(x-i, y) 
   
    x=x-(5*rep)    
def moveRight(int):
    for i in range(0, rep*5, 1):
        point(x+i, y) 
   
    x=x+(5*rep)                        

def moveUp(int):
    for i in range(0, rep*5, 1):
        point(x, y-i) 
   
    y=y-(5*rep)  

def moveDown(int):
    for i in range(0, rep*5, 1):
        point(x,y+i) 
   
    y=y+(5*rep)                           

def mouseClicked():
    saveFrame("line-######.png") 
  
def keyPressed():
    if (key == CODED) :
        if (keyCode == RIGHT) :
            moveRight(1)
            else (keyCode == DOWN):
                moveDown(1)
            else if (keyCode == UP) :
                moveup(1)
            else if (keyCode == LEFT) :
                moveleft(1)                           