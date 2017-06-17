# author: Daisy Wong, Ayushi Patel


import turtle  # turtle graphics library for drawing
import random  # math library for random number generation

degreeOfTurn = 18  # degree for the turtle to turn after drawing a shape. This determines how dense the final line art is
numOfShapes = 360 / degreeOfTurn
speedOfDrawing = 1000000000000000000000000   # increase to drawing faster
colorList = ["red", "blue", "lightGreen", "purple", "orange", "yellow", "lightBlue", "cyan", "turquoise",
             "pink", "lightBlue"]
shapeList = ["classic", "turtle", "arrow", "circle", "square", "triangle"]

# You are to design and implement a generalized polygon drawing function, returns nothing
def draw_polygon(a_turtle, sides, length):
    for x in range(sides):
        a_turtle.forward(length)
        a_turtle.right(360.0/sides)

# chooses a random color from a list of colors
def randomize_color():
    return random.choice(colorList)

# chooses a random shape for turtle from a list of shapes
def randomize_shape():
    return random.choice(shapeList)

def draw_art():
    window = turtle.Screen()
    brad = turtle.Turtle()
    brad.speed(speedOfDrawing)
    brad.pensize(2)

    # Add a loop to draw polygons for "numOfShapes" times, and turn the turtle right by "degreeOfTurn" between each time to create a pretty line art
    for a in range(25):
        window.bgcolor(randomize_color())
        brad.color(randomize_color())
        brad.shape(randomize_shape())
        numOfSides = random.randint(3, 8)  # number of sides in the polygon
        sideLength = random.randint(10, 100)  # change to use a random number between 10 and 100
        print(numOfSides)
        for y in range(int(numOfShapes)):
            draw_polygon(brad, numOfSides, sideLength)
            brad.right(degreeOfTurn)
    window.exitonclick()


# execute the line art drawing function
draw_art()
