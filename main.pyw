# Python Graphing Calculator
# Version 1.37
# Import Libraries
import turtle, math, os, pyautogui

# "Move" Subroutine
def move(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    
turtle = turtle.Turtle()

window = turtle.screen
window.setup(620,620)
window.title("Main Graph")
window.tracer(False)

# Create Grid
# Create X Axis and Y Axis
turtle.width(3)
move(300, 0)
turtle.setx(-300)
move(0, 0)
move(0, 300)
turtle.sety(-300)
# Create Vertical Gridlines
turtle.width(1)
move(-300, -300)
turtle.sety(300)
turtle.setx(300)
turtle.sety(-300)
turtle.setx(-300)

# Draw Vertical Gridlines
for offset in range(-15, 15):
    move(offset * 20, 300)
    turtle.sety(-300)
# Draw Horizontal Gridlines
for offset in range(-15, 15):
    move(300, offset * 20)
    turtle.setx(-300)

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
            slope = eval(pyautogui.prompt(title='Slope: '))
            intercept = eval(pyautogui.prompt(title='Intercept: '))
                
            # Create Angled Line
            move(-300, -20 * ((15 * slope) + intercept))
            turtle.goto(300, 20 * ((15 * slope) + intercept))

        # Straight Line Input
        if lineType == "Straight":
            axis = pyautogui.prompt(title='Axis: (X or Y)')
            intercept = eval(pyautogui.prompt(title='Intercept'))
            if axis == "y":
                move(-300, intercept * 20)
                turtle.setx(300)
            if axis == "x":
                move(intercept * 20, -300)
                turtle.sety(300)

    # Parabola Input
    if graphType == "Parabola":
        functionType = pyautogui.confirm(title='Trig Type', buttons=['X', 'Y'])
        slope = eval(pyautogui.prompt(title='Slope: '))
        intercept = eval(pyautogui.prompt(title='Intercept: '))
        # Create Parabola
        if functionType == "Y":
            for x in range(-30, 30):
                y = ((x ** 2) * slope) + intercept
                if x == -30:
                    move(x * 20, y * 20)
                else:
                    turtle.goto(x * 20, y * 20)
        if functionType == "X":
            for y in range(-30, 30):
                x = ((y ** 2) * slope) + intercept
                if x == -30:
                    move(x * 20, y * 20)
                else:
                    turtle.goto(x * 20, y * 20)

    # Circle Input
    if graphType == "Circle":
        radius = eval(pyautogui.prompt(title='Radius: '))
        xOrigin = eval(pyautogui.prompt(title='X Point Origin: '))
        yOrigin = eval(pyautogui.prompt(title='Y Point Origin: '))
        # Create Circle
        move(xOrigin * 20, 20 * (yOrigin - radius))
        turtle.circle(radius * 20)

    # Trig Input
    if graphType == "Trig":
        trigType = pyautogui.confirm(title='Trig Type', buttons=['Sin', 'Cos'])
        functionType = pyautogui.confirm(title='Function Type: ', buttons=['x', 'y'])
        a = eval(pyautogui.prompt(title='Amplitude (a)'))
        b = eval(pyautogui.prompt(title='Frequency (b)'))
        c = eval(pyautogui.prompt(title='Horizontal Shift (c)'))
        d = eval(pyautogui.prompt(title='Vertical Shift (d)'))
        if functionType == "Y":
            for x in range(-15, 16):
                if trigType == "Sin":
                    y = a * math.sin((b * x) + c) + d
                if trigType == "Cos":
                    y = a * math.cos((b * x) + c) + d
                if x == -15:
                    move(x * 20, y * 20)
                else:
                    turtle.goto(x * 20, y * 20)

        if functionType == "X":
            for y in range(-15, 16):
                if trigType == "Sin":
                    x = a * math.sin((b * y) + c) + d
                if trigType == "Cos":
                    x = a * math.cos((b * y) + c) + d
                if y == -15:
                    move(x * 20, y * 20)
                else:
                    turtle.goto(x * 20, y * 20)

    # Settings
    if graphType == "Settings":
        settingsType = pyautogui.confirm(title="What Setting Would You Like To Change?", buttons=["Line Width", "Line Color", "Reset to Default Settings"])

        if settingsType == "Line Width":
            lineWidth = eval(pyautogui.prompt(title="Line Width: "))

        if settingsType == "Line Color":
            customColor = pyautogui.confirm(title="Line Color:", buttons=["Black", "Blue", "Red", "Yellow", "Green"])

        if settingsType == "Reset to Default Settings":
            lineWidth = 1
            customColor = "black"

    # Save (Screenshot)
    if graphType == "Save":
        pyautogui.alert(text="Move other windows/popups out of the way", title="Warning!", button="OK")
        screenshot = pyautogui.screenshot(os.environ['USERPROFILE'] + "/Desktop/Graph.png")
        pyautogui.alert(text="Screenshot saved", title="Alert", button="OK")

    move(0, 0)
