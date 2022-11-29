# Python Graphing Calculator
# Version 1.35
# Import Libraries
from turtle import (speed, hideturtle, width, sety, done, setx, color, showturtle)
from Logarithms import (move, AngledLine, StraightLine, Parabola, DrawCircle, Trig)
import pyautogui

hideturtle()
# Create Grid
speed(0)
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
drawSpeed = 0
lineWidth = 2
customColor = "black"
cursorVisibility = "Hide"

if __name__ == "__main__":
    while graphType != "Finish":
        # Reset Graph Values
        speed(drawSpeed)
        width(lineWidth)
        color(customColor)
        if cursorVisibility == "Show":
            showturtle()
        if cursorVisibility == "Hide":
            hideturtle()

        # Graph Type Input
        graphType = pyautogui.confirm(title="Graph Type:", buttons=["Line", "Parabola", "Circle", "Trig", "Settings", "Finish"])

        # Line Input
        if graphType == "Line":
            lineType = pyautogui.confirm(title="Angle or Straight Line?", buttons=["Angled", "Straight"])

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
        if graphType == "Settings":
            settingsType = pyautogui.confirm(title="What Setting Would You Like To Change?", buttons=["Line Width", "Cursor Speed", "Line Color", "Cursor Visibility", "Reset to Default Settings"])

            if settingsType == "Line Width":
                lineWidth = eval(pyautogui.prompt(title="Line Width: "))

            if settingsType == "Cursor Speed":
                drawSpeed = eval(pyautogui.prompt(title="Cursor Speed: "))

            if settingsType == "Line Color":
                customColor = pyautogui.prompt(title="Line Color: ")

            if settingsType == "Cursor Visibility":
                cursorVisibility = pyautogui.confirm(title="Cursor Visibility:", buttons=["Show", "Hide"])
                if cursorVisibility == "Show":
                    showturtle()
                if cursorVisibility == "Hide":
                    hideturtle()

            if settingsType == "Reset to Default Settings":
                width(1)
                speed(0)
                color("black")
                hideturtle()
                
        print()
        move(0, 0)

done()
