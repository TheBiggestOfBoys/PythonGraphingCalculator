# Python Graphing Calculator
# Version 1.33
# Import Libraries
from turtle import (speed, hideturtle, width, sety, done, setx)
from Logarithms import (move, AngledLine, StraightLine, Parabola, DrawCircle, Trig)
import pyautogui

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

        print()
        move(0, 0)

done()
