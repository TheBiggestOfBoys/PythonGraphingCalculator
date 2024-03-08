# Python Graphing Calculator
# Version 1.39
# Import Libraries
import math
import os
import turtle
import pyautogui


# "Move" Subroutine
def move(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()


resolution = eval(pyautogui.prompt(title="Enter grid resolution"))

turtle = turtle.Turtle()

window = turtle.screen
window.screensize(600, 600)
window.setworldcoordinates(-resolution, -resolution, resolution, resolution)
window.title("Main Graph")
window.tracer(False)
turtle.hideturtle()

# Create Grid
# Create X Axis and Y Axis
turtle.width(3)
move(resolution, 0)
turtle.setx(-resolution)
move(0, 0)
move(0, resolution)
turtle.sety(-resolution)

# Create Vertical Gridlines
turtle.width(1)
move(-resolution, -resolution)
turtle.sety(resolution)
turtle.setx(resolution)
turtle.sety(-resolution)
turtle.setx(-resolution)

# Draw Vertical Gridlines
for offset in range(-resolution, resolution + 1):
    move(offset, resolution)
    turtle.sety(-resolution)

# Draw Horizontal Gridlines
for offset in range(-resolution, resolution + 1):
    move(resolution, offset)
    turtle.setx(-resolution)

move(0, 0)
graphType = ""
lineWidth = 2
customColor = "black"

while graphType != "Finish":
    # Reset Graph Values
    turtle.width(lineWidth)
    turtle.color(customColor)

    # Graph Type Input
    graphType = pyautogui.confirm(title="Graph Type:", buttons=["Line", "Parabola", "Circle", "Trig", "Settings", "Save", "Finish"])

    # Line Input
    if graphType == "Line":
        lineType = pyautogui.confirm(title="Angle or Straight Line?", buttons=["Angled", "Straight"])

        # Angled Line Input
        if lineType == "Angled":
            slope = eval(pyautogui.prompt(title="Slope"))
            intercept = eval(pyautogui.prompt(title="Intercept"))

            # Create Angled Line
            move(-resolution, (resolution * slope) + intercept)
            turtle.goto(resolution, -((resolution * slope) + intercept))

        # Straight Line Input
        if lineType == "Straight":
            axis = pyautogui.confirm(title="Axis", buttons=["X", "Y"])
            intercept = eval(pyautogui.prompt(title="Intercept"))
            if axis == "Y":
                move(-resolution, intercept)
                turtle.setx(resolution)
            if axis == "X":
                move(intercept, -resolution)
                turtle.sety(resolution)

    # Parabola Input
    if graphType == "Parabola":
        functionType = pyautogui.confirm(title="Parabola Type", buttons=["X", "Y"])
        slope = eval(pyautogui.prompt(title="Slope"))
        intercept = eval(pyautogui.prompt(title="Intercept"))
        # Create Parabola
        if functionType == "Y":
            for x in range(-resolution, resolution + 1):
                y = ((x ** 2) * slope) + intercept
                if x == -resolution:
                    move(x, y)
                else:
                    turtle.goto(x, y)
        if functionType == "X":
            for y in range(-resolution, resolution + 1):
                x = ((y ** 2) * slope) + intercept
                if x == -resolution:
                    move(x, y)
                else:
                    turtle.goto(x, y)

    # Circle Input
    if graphType == "Circle":
        radius = eval(pyautogui.prompt(title="Radius"))
        xOrigin = eval(pyautogui.prompt(title="X Point Origin"))
        yOrigin = eval(pyautogui.prompt(title="Y Point Origin"))
        # Create Circle
        move(xOrigin, yOrigin - radius)
        turtle.circle(radius, None, resolution)

    # Trig Input
    if graphType == "Trig":
        trigType = pyautogui.confirm(title="Trig Type", buttons=["Sin", "Cos"])
        functionType = pyautogui.confirm(title="Function Type", buttons=["X", "Y"])
        a = eval(pyautogui.prompt(title="Amplitude (a)"))
        b = eval(pyautogui.prompt(title="Frequency (b)"))
        c = eval(pyautogui.prompt(title="Horizontal Shift (c)"))
        d = eval(pyautogui.prompt(title="Vertical Shift (d)"))
        if functionType == "Y":
            for x in range(-resolution, resolution + 1):
                if trigType == "Sin":
                    y = a * math.sin((b * x) + c) + d
                if trigType == "Cos":
                    y = a * math.cos((b * x) + c) + d
                if x == -resolution:
                    move(x, y)
                else:
                    turtle.goto(x, y)

        if functionType == "X":
            for y in range(-resolution, resolution + 1):
                if trigType == "Sin":
                    x = a * math.sin((b * y) + c) + d
                if trigType == "Cos":
                    x = a * math.cos((b * y) + c) + d
                if y == -resolution:
                    move(x, y)
                else:
                    turtle.goto(x, y)

    # Settings
    if graphType == "Settings":
        settingsType = pyautogui.confirm(title="What Setting Would You Like To Change?", buttons=["Line Width", "Line Color", "Reset to Default Settings"])

        if settingsType == "Line Width":
            lineWidth = eval(pyautogui.prompt(title="Line Width"))

        if settingsType == "Line Color":
            customColor = pyautogui.confirm(title="Line Color:", buttons=["Black", "Blue", "Red", "Yellow", "Green"])

        if settingsType == "Reset to Default Settings":
            lineWidth = 1
            customColor = "black"

    # Save (Screenshot)
    if graphType == "Save":
        pyautogui.alert(text="Move other windows/popups out of the way", title="Warning!", button="OK")
        screenshot = pyautogui.screenshot(os.environ["USERPROFILE"] + "/Desktop/Graph.png")
        pyautogui.alert(text="Screenshot saved", title="Alert", button="OK")

    move(0, 0)
