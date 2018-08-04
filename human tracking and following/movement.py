# these are the paramenters for ideal human image
yCentre = 300                  # y ideal
yHeight = 420                 # y+h
xCentre = 300                # x ideal
xWidth = 400                 # x+w
area = (xCentre - xWidth) * (yCentre - yHeight)   # computing area of the block
centerX = (xCentre + xWidth) / 2      # finding ideal x center
centerY = (yCentre + yHeight) / 2     # finding ideal y center

def moveForward():
    print("Moving forward")          # all forward movement code with high speed
def stopMoving():
    print("Movement Stopped")         # sudden movement stopped
def moveRight():
    print("rightward movement")       # rightward movement with less speed and curvy path  means left wheel will have higher rotation
def moveLeft():
    print("leftward mpvement")       # leftward movement with less speed and curvy path means right wheel will have higher rotation

def minimiseError(x, y, xw, yh):         # the function for movement decision....based on PID not total
    centerImgX = (x + xw) / 2
    centerImgY = (y + yh) / 2
    areaImg = (xw - x) * (yh - y)
    if (areaImg < area and abs(centerX-centerImgX)<=50 and abs(centerY-centerImgX)<=50):
        moveForward()
    elif(areaImg>=area):
        stopMoving()
    if(centerX-centerImgX>50):
        moveLeft()
    elif(centerX-centerImgX<50):
        moveRight()