# Python Graphing Calculator
# Version 1.33
# Import Libraries
from turtle import (speed, hideturtle, width, sety, done, setx, color)
from Logarithms import (move, AngledLine, StraightLine, Parabola, DrawCircle, Trig)
import pyautogui

if cursorVisibility == True:
    showturtle()
if cursorVisibility == False:
    hideturtle()

# Create Grid
speed(0)
hideturtle()
print("Drawing Graph...")
# Create X Axis and Y Axis
print("Creating X Axis and Y Axis")
width(3)
move(300, 0)
setx(-300)
move(0, 0)
move(0, 300)
sety(-300)

# Create Vertical Gridlines
print("Creating Gridlines")
width(1)
move(-300, -300)
sety(300)
setx(300)
sety(-300)
setx(-300)

# Draw Vertical Gridlines
for offset in range(-15, 15):
    move(offset * 20, 300)
    sety(-300)
# Draw Horizontal Gridlines
for offset in range(-15, 15):
    move(300, offset * 20)
    setx(-300)

print("Done!")
print()
move(0, 0)
graphType = ""
width(2)

if __name__ == '__main__':
    while graphType != "Finish":
        # Graph Type Input
        graphType = pyautogui.confirm(title='Graph Type:', buttons=['Line', 'Parabola', 'Circle', 'Trig', 'Finish'])

        # Line Input
        if graphType == "Line":
            lineType = pyautogui.confirm(title='Angle or Straight Line?', buttons=['Angled', 'Straight'])

            # Angled Line Input
            if lineType == "Angled":
                AngledLine()

            # Straight Line Input
            if lineType == "Straight":
                StraightLine()

        # Parabola Input
        if graphType == "Parabola":
            Parabola()

        # Circle Input
        if graphType == "Circle":
            DrawCircle()

        # Trig Input
        if graphType == "Trig":
            Trig()

        # Settings
        if graphType == ("6" or "Settings"):
            print("Changeable Setting:")
            print("1 = Line Width")
            print("2 = Cursor Speed")
            print("3 = Line Color")
            print("4 = Cursor Shape")
            print("5 = Grid Size")
            print("6 = Toggle Cursor Visibility")
            print("7 = Reset to Default Settings")

            settingsType = input("What Setting Would You Like To Change? ")

            if settingsType == ("1" or "Line Width" or "Width"):
                lineWidth = eval(input("Line Width: "))

            if settingsType == ("2" or "Cursor Speed" or "Speed"):
                drawSpeed = eval(input("Cursor Speed: "))

            if settingsType == ("3" or "Line Color" or "Color"):
                customColor = input("Line Color: ")

            if settingsType == ("4" or "Cursor Shape" or "Shape"):
                cursorShape = input("Cursor Shape: ")

            if settingsType == ("5" or "Grid Size" or "Size"):
                size = eval(input("Grid Size: "))

            if settingsType == ("6" or "Toggle Cursor Visibility" or "Cursor Visibility"):
                if cursorVisibility == True:
                    hideturtle()
                if cursorVisibility == False:
                    showturtle()
            if settingsType == ("7" or "Reset" or "Default Settings"):
                width(1)
                speed(0)
                color('black')

        print()
        move(0, 0)

done()
