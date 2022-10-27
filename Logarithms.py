from turtle import (setx, sety, up, down, goto, circle)

# Logarithms
# Move
def move(x, y):
    up()
    goto(x, y)
    down()

# Reset Turtle
def resetTurtle():
    print()
    move(0, 0)

# Circle
def DrawCircle():
    radius = eval(input("Radius: "))
    xOrigin = eval(input("X Point Origin: "))
    yOrigin = eval(input("Y Point Origin: "))
    print("(x -", xOrigin, ")² + (y -", yOrigin, ")² =", radius, "²", "(", radius ** 2, ")")
    # Create Circle
    move((xOrigin * 20), (20 * (yOrigin - radius)))
    circle(radius * 20)

# Parabola
def Parabola():
    print("1: y = , 2: x =")
    functionType = input("Function Type: ")
    slope = eval(input("Slope: "))
    intercept = eval(input("Intercept: "))
    print("y =", slope, "*x^2 +", intercept)
    # Create Parabola
    print("Points: ")
    if functionType == ("1" or "y"):
        for x in range(-30, 30):
            y = (((x ** 2) * slope) + intercept)
            if x == -30:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)
            return x, y
    if functionType == ("2" or "x"):
        for y in range(-30, 30):
            x = (((y ** 2) * slope) + intercept)
            if x == -30:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)
            return x, y

def AngledLine():
    slope = eval(input("Slope: "))
    intercept = eval(input("Intercept: "))
    print("Equation: y =", slope, "*x +", intercept)
    # Create Angled Line
    move(-300, 20 * -((15 * slope) + intercept))
    goto(300, 20 * ((15 * slope) + intercept))
    print("Points: ")
    for x in range(-15, 16):
        return x, ((x * slope) + intercept)

def StraightLine():
    print("Type y for 'y =' | x for 'x ='")
    axis = input("Axis: ")
    print(axis, "Axis Intercept: ", end='')
    intercept = eval(input())
    print(axis, "=", intercept)
    if axis == "y":
        move(-300, intercept * 20)
        setx(300)
        print("Points: ")
        for y in range(-15, 16):
            return intercept, y
    if axis == "x":
        move(intercept * 20, -300)
        sety(300)
        print("Points: ")
        for x in range(-15, 16):
            return x, intercept

def Trig():
    from math import (sin, cos)
    print("Enter 'Sin' or 'Cos'")
    trigType = input("Trig Graph Type: ")
    print("1: y = , 2: x =")
    functionType = input("Function Type: ")
    a = eval(input("Amplitude (a) = "))
    b = eval(input("Frequency (b) = "))
    c = eval(input("Horizontal Shift (c) = "))
    d = eval(input("Vertical Shift (d) = "))
    if functionType == ("1" or "y"):
        for x in range(-15, 16):
            if trigType == "Sin":
                y = a * sin((b * x) + c) + d
            if trigType == "Cos":
                y = a * cos((b * x) + c) + d
            if x == -15:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)

    if functionType == ("2" or "x"):
        for y in range(-15, 16):
            if trigType == "Sin":
                x = a * sin((b * y) + c) + d
            if trigType == "Cos":
                x = a * cos((b * y) + c) + d
            if y == -15:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)

    print("Equation: y =", a, trigType, "(", b, "x +", c, ") +", d)

def GraphPoints():
    XPoints = open("XPoints.txt", 'r')
    YPoints = open("YPoints.txt", 'r')

    print(eval(XPoints.readline(1)) + 2)

    for point in range(10):
        print("(", XPoints.readline(point), ",", YPoints.readline(point), ")")
        if point == 0:
            move(eval(XPoints.readline(point)) * 20, eval(YPoints.readline(point)) * 20)
        else:
            goto(eval(XPoints.readline(point)) * 20, eval(YPoints.readline(point)) * 20)

    XPoints.close()
    YPoints.close()