#####################################################################
# Game Program: Escape
# By: Ryan Wu
# Teacher: Mr. Schattman
# Course: ICS 3UI 
#####################################################################

# Imports
from tkinter import *
from math import *
from time import *
from random import *
import time

# Creates Screen
root = Tk()
s = Canvas(root, width=800, height=800, background="white")

# Sets all the initial values that are needed throughout the program
# Also imports images used in the program
def setInitialValues():
    global xStart, yStart, xSpeed, ySpeed, Qpressed, xPortal, yPortal, Mercedes, MercedesR, MercedesL
    global startJump, g, v, jumpTime, inAir, groundLevel, height, Warrior, Underwater, WateryPlatform
    global xPlat, yPlat, alive, win, onPlat, screen, yClick, xClick
    xStart = 350
    groundLevel = 725
    height = 71 
    yStart = groundLevel - height
    xSpeed = 0
    ySpeed = 0
    xPortal = 700
    yPortal = 110
    onPlat = False
    g = 0
    v = 0
    jumpTime = 0
    inAir = False
    Warrior = PhotoImage(file = "Warrior.gif")
    startJump = False
    Qpressed = False
    win = False
    alive = True
    screen = "menu"
    xClick = None
    yClick = None
    xPlat = [365,400,725,675,123,150,450]
    yPlat = [750,500,250,550,600,400,325]
    Underwater = PhotoImage(file = "Underwater_.gif")
    s.create_image(400,400, image = Underwater)
    WateryPlatform = PhotoImage(file = "UnderwaterPlatform_.gif")
    s.create_image(365,750, image = WateryPlatform)
    s.create_image(400,500, image = WateryPlatform)
    s.create_image(725,250, image = WateryPlatform)
    s.create_image(675,550, image = WateryPlatform)
    s.create_image(123,600, image = WateryPlatform)
    s.create_image(150,400, image = WateryPlatform)
    s.create_image(450,325, image = WateryPlatform)

# Determines if the player has jumped off into the abyss or their y-position is greater than 800 which is the end of the screen
def determineGameOutcome():
    global yStart
    if yStart >= 800:
        alive = False
        win = False
        endscreen()

# Creates the end screen, the same outcome whether the player wins or now
# Allows the player to play again or quit
def endScreen():
    global screen, ez, ez1, ez2, ez3, ez4, ez5
    ez = s.create_rectangle(200,200,600,600, fill = "white", outline = "red", width = 10)
    ez1 = s.create_text(240,300, text = "PLAY AGAIN?", font = "times 50", fill = "red", anchor = W)
    ez2 = s.create_rectangle(240,400,390,500, fill = "white", outline = "red", width = 10)
    ez3 = s.create_text(265,450, text = "YES", font = "times 50", fill = "red", anchor = W)
    ez4 = s.create_rectangle(415,400,560,500, fill = "white", outline = "red", width = 10)
    ez5 = s.create_text(452,450, text = "NO", font = "times 50", fill = "red", anchor = W)
    if xClick != None:
        if xClick >= 240 and xClick <= 390 and yClick >= 400 and yClick <= 500:
            screen = "menu"
            setInitialValues()
        elif xClick >= 415 and xClick <= 560 and yClick >= 400 and yClick <= 500:
            stopGame()

# Creates the start screen
# Allows the player to select between difficulties
# Also sets the timer determined by the difficulty
def startScreen():
    global screen, A, B, C, D, E, F, curry_Time, timeLimit
    A = s.create_rectangle(200,760,600,660, fill = "white", outline = "red", width = "10")
    B = s.create_text(330,710, text = "HARD", font = "Times 50", fill = "red", anchor = W) 
    C = s.create_rectangle(200,600,600,500, fill = "white", outline = "red", width = "10")
    D = s.create_text(300, 550, text = "MEDIUM", font = "Times 50", fill = "red", anchor = W)
    E = s.create_rectangle(200,440,600,340, fill = "white", outline = "red", width = "10")
    F = s.create_text(340,390, text = "EASY", font = "Times 50", fill = "red", anchor = W)
    if xClick != None:
        if xClick >= 200 and xClick <= 600 and yClick >= 660 and yClick <= 760:
            screen = "gameStart"
            curry_Time = time.time()
            timeLimit = 30
            s.delete(A, B, C, D, E, F)
        elif xClick >= 200 and xClick <= 600 and yClick >= 500 and yClick <= 600:
            screen = "gameStart"
            curry_Time = time.time()
            timeLimit = 45
            s.delete(A, B, C, D, E, F)
        elif xClick >= 200 and xClick <= 600 and yClick >= 340 and yClick <= 440:
            screen = "gameStart"
            curry_Time = time.time()
            timeLimit = 60
            s.delete(A, B, C, D, E, F)

# Determines the time of the game
# If time runs out on the player it ends the game
def curryTime():
    global potato_Time, screen
    potato_Time = s.create_text(50,50, text = int(timeLimit - (time.time() - curry_Time)), font = "Times 50", fill = "white")
    if timeLimit - (time.time() - curry_Time) <= 0:
        screen = "endScreen"

# Determines the position where the player has clicked with their mouse
def mouseClick( event ):
    global xClick, yClick
    xClick = event.x
    yClick = event.y  

# Checks to see if the player is on a platform
def checkPlatforms():
    global xStart, yStart, xSpeed, ySpeed, startJump, onPlat
    for f in range(len(xPlat)):
        if xStart > xPlat[f] - 100 and xStart  < xPlat[f] + 100:
            if yStart + 75 == yPlat[f]:
                yStart = yStart - 0.5
                onPlat = True

        else:
            startJump = True
            onPlat = False

# Creates the playable character
def drawWarrior():
    global Warrior, xStart, yStart
    Warrior = PhotoImage(file = "Warrior.gif")
    if alive == True:
        s.create_image(xStart,yStart, image = Warrior)

# Creates the portal and determines if the player has reached it or not
def drawPortal():
    global Portal, xPortal, yPortal, xStart, yStart, alive, Warrior, win, screen
    Portal = PhotoImage(file = "rsz_1portal.gif")
    s.create_image(xPortal,yPortal, image = Portal)
    if xStart >= 604 and xStart <=796:
        if yStart >= 14 and yStart <=206:
            alive = False
            s.delete(Warrior)
            win = True
            screen = "endScreen"

# Stops the game
def stopGame():
    root.destroy()

# Supposed to determine the end of the jump parabola
def justLanded():
    if onPlat == True and inAir == True:
        return True
    else:
        return False

# Determines the course of action based on what key the player clicks
def keyDownHandler ( event ):
    global ySpeed, xSpeed, Qpressed, yStart, startJump, g, v, inAir

    if event.keysym == "space":
        startJump = True
##        g = 0.3
##        v = 15
##        inAir = True
        yStart = yStart - 50
    if event.keysym == "Left":
        xSpeed = -5

    if event.keysym == "Right":
        xSpeed = +5
    
    if event.keysym == "q" or event.keysym == "Q":
        Qpressed = True

# Updates the character's position
def updateWarrior():
    global xSpeed, ySpeed, xStart, yStart, g, v, jumpTime, inAir, screen
    xStart = xStart + xSpeed
    g*jumpTime**2 - v*jumpTime + groundLevel - height
    if justLanded() == True:
        inAir = False
        g = 0
        v = 0
        yStart = groundLevel - height
        jumpTime = 0
    
    if startJump == True:
        yStart = yStart + 0.5

    if yStart >= 870:
       screen = "endScreen"

# Runs the game
def runGame():
    global jumpTime, xClick, yClick
    setInitialValues()
    while True:
        while screen == "gameStart":
            curryTime()
            checkPlatforms()
            updateWarrior()
            drawPortal()
            drawWarrior()
##                if inAir == True:
##                    jumpTime = jumptime + 1
            
            s.update()
            sleep(0.01)
            s.delete(Warrior, potato_Time)
        if screen == "endScreen":
            endScreen()
            s.update()
            s.delete(ez, ez1, ez2, ez3, ez4, ez5)

        elif screen == "menu":
            startScreen()
            s.update()
            s.delete(A, B, C, D, E, F)

 #       xClick = None
 #       yClick = None

root.after(0, runGame)

s.bind( "<Key>", keyDownHandler)
s.bind( "<Button-1>", mouseClick)

##s.bind( "<KeyRelease>", keyUpHandler)

s.pack()
s.focus_set()
root.mainloop()

    
