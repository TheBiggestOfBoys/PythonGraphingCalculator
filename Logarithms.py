from turtle import (setx, sety, up, down, goto, circle)
from math import (sin, cos)
import pyautogui

# Move
def move(x, y):
    up()
    goto(x, y)
    down()

# Circle
def DrawCircle():
    radius = eval(pyautogui.prompt(title='Radius: '))
    xOrigin = eval(pyautogui.prompt(title='X Point Origin: '))
    yOrigin = eval(pyautogui.prompt(title='Y Point Origin: '))
    print("(x -", xOrigin, ")² + (y -", yOrigin, ")² =", radius, "²", "(", radius ** 2, ")")
    # Create Circle
    move(xOrigin * 20, 20 * (yOrigin - radius))
    circle(radius * 20)

# Parabola
def Parabola():
    functionType = pyautogui.confirm(title='Trig Type', buttons=['X', 'Y'])
    slope = eval(pyautogui.prompt(title='Slope: '))
    intercept = eval(pyautogui.prompt(title='Intercept: '))
    # Create Parabola
    print("Points: ")
    if functionType == "Y":
        print("y =", slope, "x²", "+", intercept)
        for x in range(-30, 30):
            y = ((x ** 2) * slope) + intercept
            if x == -30:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)
            print("(", x, ",", y, ")", end=' ')
    if functionType == "X":
        print("x =", slope, "*y²", "+", intercept)
        for y in range(-30, 30):
            x = ((y ** 2) * slope) + intercept
            if x == -30:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)
            print("(", x, ",", y, ")", end=' ')

def AngledLine():
    slope = eval(pyautogui.prompt(title='Slope: '))
    intercept = eval(pyautogui.prompt(title='Intercept: '))
    print("Equation: y =", slope, "x +", intercept)
    # Create Angled Line
    move(-300, 20 * -((15 * slope) + intercept))
    goto(300, 20 * ((15 * slope) + intercept))
    print("Points: ")
    for x in range(-15, 16):
        print("(", x, ",", ((x * slope) + intercept), ")")

def StraightLine():
    axis = pyautogui.prompt(title='Axis: (X or Y)')
    intercept = eval(pyautogui.prompt(title='Intercept'))
    print(axis, "=", intercept)
    if axis == "y":
        move(-300, intercept * 20)
        setx(300)
        print("Points: ")
        for y in range(-15, 16):
            print(intercept, y)
    if axis == "x":
        move(intercept * 20, -300)
        sety(300)
        print("Points: ")
        for x in range(-15, 16):
            print(x, intercept)

def Trig():
    trigType = pyautogui.confirm(title='Trig Type', buttons=['Sin', 'Cos'])
    functionType = pyautogui.confirm(title='Function Type: ', buttons=['X', 'Y'])
    a = eval(pyautogui.prompt(title='Amplitude (a)'))
    b = eval(pyautogui.prompt(title='Frequency (b)'))
    c = eval(pyautogui.prompt(title='Horizontal Shift (c)'))
    d = eval(pyautogui.prompt(title='Vertical Shift (d)'))
    if functionType == "Y":
        for x in range(-15, 16):
            if trigType == "Sin":
                y = a * sin((b * x) + c) + d
            if trigType == "Cos":
                y = a * cos((b * x) + c) + d
            if x == -15:
                move(x * 20, y * 20)
            else:
                goto(x * 20, y * 20)

    if functionType == "X":
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
