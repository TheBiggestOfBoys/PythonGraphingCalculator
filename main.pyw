# Python Graphing Calculator
# Version 1.39
# Import Libraries
import math
import turtle

turtle = turtle.Turtle()
turtle.hideturtle()
turtle.speed(0)

# "Move" Subroutine
def move(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_axis(resolution):
    turtle.width(3)
    move(resolution, 0)
    turtle.setx(-resolution)
    move(0, 0)
    move(0, resolution)
    turtle.sety(-resolution)

def draw_gridlines(resolution):
    turtle.width(1)
    move(-resolution, -resolution)
    turtle.sety(resolution)
    turtle.setx(resolution)
    turtle.sety(-resolution)
    turtle.setx(-resolution)
    for offset in range(-resolution, resolution + 1):
        move(offset, resolution)
        turtle.sety(-resolution)
    for offset in range(-resolution, resolution + 1):
        move(resolution, offset)
        turtle.setx(-resolution)

def get_float_input(prompt_title):
    return float(turtle.screen.textinput("Input", prompt_title))

def get_confirm_input(prompt_title, buttons):
    return turtle.screen.textinput("Input", f"{prompt_title} ({'/'.join(buttons)})")

def draw_line():
    lineType = get_confirm_input("Angle or Straight Line?", ["Angled", "Straight"])
    if lineType == "Angled":
        slope = get_float_input("Slope")
        intercept = get_float_input("Intercept")
        move(-resolution, (resolution * slope) + intercept)
        turtle.goto(resolution, -((resolution * slope) + intercept))
    elif lineType == "Straight":
        axis = get_confirm_input("Axis", ["X", "Y"])
        intercept = get_float_input("Intercept")
        if axis == "Y":
            move(-resolution, intercept)
            turtle.setx(resolution)
        elif axis == "X":
            move(intercept, -resolution)
            turtle.sety(resolution)

def draw_parabola():
    functionType = get_confirm_input("Parabola Type", ["X", "Y"])
    slope = get_float_input("Slope")
    intercept = get_float_input("Intercept")
    if functionType == "Y":
        for x in range(-resolution, resolution + 1):
            y = ((x ** 2) * slope) + intercept
            if x == -resolution:
                move(x, y)
            else:
                turtle.goto(x, y)
    elif functionType == "X":
        for y in range(-resolution, resolution + 1):
            x = ((y ** 2) * slope) + intercept
            if x == -resolution:
                move(x, y)
            else:
                turtle.goto(x, y)

def draw_circle():
    radius = get_float_input("Radius")
    xOrigin = get_float_input("X Point Origin")
    yOrigin = get_float_input("Y Point Origin")
    move(xOrigin, yOrigin - radius)
    turtle.circle(radius, None, resolution)

def draw_trig():
    trigType = get_confirm_input("Trig Type", ["Sin", "Cos"])
    functionType = get_confirm_input("Function Type", ["X", "Y"])
    a = get_float_input("Amplitude (a)")
    b = get_float_input("Frequency (b)")
    c = get_float_input("Horizontal Shift (c)")
    d = get_float_input("Vertical Shift (d)")
    if functionType == "Y":
        for x in range(-resolution, resolution + 1):
            y = a * (math.sin if trigType == "Sin" else math.cos)((b * x) + c) + d
            if x == -resolution:
                move(x, y)
            else:
                turtle.goto(x, y)
    elif functionType == "X":
        for y in range(-resolution, resolution + 1):
            x = a * (math.sin if trigType == "Sin" else math.cos)((b * y) + c) + d
            if y == -resolution:
                move(x, y)
            else:
                turtle.goto(x, y)

def change_settings():
    settingsType = get_confirm_input("What Setting Would You Like To Change?", ["Line Width", "Line Color", "Reset to Default Settings"])
    if settingsType == "Line Width":
        turtle.width(get_float_input("Line Width"))
    elif settingsType == "Line Color":
        turtle.color(get_confirm_input("Line Color:", ["Black", "Blue", "Red", "Yellow", "Green"]))
    elif settingsType == "Reset to Default Settings":
        turtle.width(2)
        turtle.color("black")

resolution = int(turtle.screen.textinput("Input", "Enter grid resolution"))

turtle.screen.tracer(False)
turtle.screen.screensize(600, 600)
turtle.screen.setworldcoordinates(-resolution, -resolution, resolution, resolution)
turtle.screen.title("Main Graph")

draw_axis(resolution)
draw_gridlines(resolution)

turtle.width(2)
turtle.color("black")

graphType = ""

while graphType != "Finish":
    move(0, 0)
    graphType = get_confirm_input("Graph Type:", ["Line", "Parabola", "Circle", "Trig", "Settings", "Finish"])
    if graphType == "Line":
        draw_line()
    elif graphType == "Parabola":
        draw_parabola()
    elif graphType == "Circle":
        draw_circle()
    elif graphType == "Trig":
        draw_trig()
    elif graphType == "Settings":
        change_settings()
