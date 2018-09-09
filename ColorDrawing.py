#Python version: 3.7
import turtle
side = input("Please enter the number of sides: ")
red = input("Input red value: ")
green = input("Input green value: ")
blue = input("Input blue value: ")
if float(red) < 0 or float(red) > 1 or float(green) < 0 or float(green) > 1 or float(blue) < 0 or float(blue) > 1 or float(side) < 3:
    print("Please check your input values and try again")
else:
    exteriorAngle = 180 - 180*(float(side) - 2)/float(side)
    turtle.color(float(red), float(green), float(blue))
    turtle.begin_fill()
    count = 0
    while count <= float(side):
        turtle.down()
        turtle.forward(50)
        turtle.right(exteriorAngle)
        count = count + 1
    turtle.end_fill()
    
