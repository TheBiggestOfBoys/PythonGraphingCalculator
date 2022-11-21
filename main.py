# Python Graphing Calculator
# Version 1.33
# Import Libraries
from turtle import (speed, hideturtle, width, sety, color, done, setx)
from Logarithms import (move, AngledLine, StraightLine, Parabola, DrawCircle, Trig)
import pyautogui
# Create Grid
speed(0)
hideturtle()
print("Drawing Graph...")
# Create X Axis and Y Axis
print("Creating X Axis and Y Axis")
width(3)
move(600, 0)
setx(-600)
move(0, 0)
move(0, 600)
sety(-600)

# Create Vertical Gridlines
print("Creating Gridlines")
width(1)
move(-600, -600)
sety(600)
setx(600)
sety(-600)
setx(-600)

# Draw Vertical Gridlines
for offset in range(-15, 15):
    move(offset * 40, 600)
    sety(-600)
# Draw Horizontal Gridlines
for offset in range(-15, 15):
    move(600, offset * 40)
    setx(-600)

print("Done!")
print()
move(0, 0)
graphType = ""
color("blue")

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
