X = [-3, 1, 6, 0, 5, 2, 6, 7, 8, 9]
Y = [9, -8, 7, 6, -5, -9, 3, 3, 5, 0]
from turtle import goto

print("X, Y")
for point in range(len(X)):
    print("(", X[point], ",", Y[point], ")")
    goto(X[point]*20, Y[point]*20)
