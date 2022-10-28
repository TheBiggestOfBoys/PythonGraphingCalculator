# Python Graphing Calculator
# Version 1.31
from turtle import (speed, hideturtle, width, setx, sety, color, done)
from Logarithms import move

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

# Graph Type Input
print("1 = Line | 2 = Parabola | 3 = Circle | 4 = Trig | 5 = Finish Graph | 6 = Point Graphing")

color("blue")
graphType = 0

if __name__ == '__main__':
    while graphType != ("5" or "finish"):
        graphType = input("Graph Type: ")

        # Line Input
        if graphType == ("1" or "line"):
            print("1 = Angled | 2 = Straight")
            lineType = input("Line Type: ")

            # Angled Line Input
            if lineType == ("1" or "angled"):
                from Logarithms import AngledLine
                AngledLine()

            # Straight Line Input
            if lineType == ("2" or "straight"):
                from Logarithms import StraightLine
                StraightLine()

        # Parabola Input
        if graphType == ("2" or "parabola"):
            from Logarithms import Parabola
            Parabola()

        # Circle Input
        if graphType == ("3" or "circle"):
            from Logarithms import DrawCircle
            DrawCircle()

        # Trig Input
        if graphType == ("4" or "trig"):
            from Logarithms import Trig
            Trig()

        if graphType == ("6" or "point"):
            from Logarithms import GraphPoints
            GraphPoints()

        print()
        move(0, 0)

done()
